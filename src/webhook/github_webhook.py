from fastapi import APIRouter, Request
from src.services.storage_service import save_review

from src.services.github_service import (
    get_pr_files,
    post_inline_comment
)

from src.services.ai_review_service import analyze_code

from src.analyzers.rule_based_checker import (
    run_rule_based_checks
)

from src.utils.severity import calculate_severity_score

router = APIRouter()

@router.post("/github/webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    if payload.get("action") != "opened":

        return {
            "message": "Ignored"
        }

    repo_name = payload["repository"]["full_name"]

    pr_number = payload["pull_request"]["number"]

    changed_files, commit_id = get_pr_files(
        repo_name,
        pr_number
    )

    all_issues = []

    for file in changed_files:

        diff = file["patch"]

        if not diff:
            continue

        print(f"\nReviewing File: {file['filename']}")

        # RULE-BASED CHECKS
        rule_issues = run_rule_based_checks(diff)

        # AI ANALYSIS
        ai_result = analyze_code(diff)

        # Merge all AI categories
        ai_issues = (
            ai_result["security"]
            + ai_result["performance"]
            + ai_result["bugs"]
            + ai_result["code_smells"]
        )

        issues = rule_issues + ai_issues

        all_issues.extend(issues)

        # INLINE COMMENTS
        for issue in issues:

            comment = f"""
### {issue['severity']} Issue

**Issue:** {issue['issue']}

**Explanation:**  
{issue['explanation']}

**Suggestion:**  
{issue['suggestion']}
"""

            try:

                post_inline_comment(
                    repo_name=repo_name,
                    pr_number=pr_number,
                    body=comment,
                    commit_id=commit_id,
                    path=file["filename"],
                    line=issue["line"]
                )

            except Exception as e:

                print("\nInline Comment Error\n")
                print(e)

    total_score = calculate_severity_score(all_issues)

    print("\nTOTAL RISK SCORE:", total_score)

    review_data = {
        "repository": repo_name,
        "pr_number": pr_number,
        "risk_score": total_score,
        "total_issues": len(all_issues),
        "issues": all_issues
    }

    save_review(review_data)

    return {
        "message": "Review completed",
        "risk_score": total_score,
        "total_issues": len(all_issues)
    }