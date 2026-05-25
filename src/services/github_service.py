from github import Github
from src.config.settings import settings

g = Github(settings.GITHUB_TOKEN)

def get_pr_files(repo_name, pr_number):

    repo = g.get_repo(repo_name)

    pull_request = repo.get_pull(pr_number)

    files = pull_request.get_files()

    changed_files = []

    for file in files:

        changed_files.append({
            "filename": file.filename,
            "status": file.status,
            "patch": file.patch
        })

    return changed_files, pull_request.head.sha


def post_inline_comment(
    repo_name,
    pr_number,
    body,
    commit_id,
    path,
    line
):

    repo = g.get_repo(repo_name)

    pull_request = repo.get_pull(pr_number)

    pull_request.create_review_comment(
        body=body,
        commit=repo.get_commit(commit_id),
        path=path,
        line=line
    )