def calculate_severity_score(issues):

    score = 0

    for issue in issues:

        severity = issue.get("severity", "LOW")

        if severity == "HIGH":
            score += 5

        elif severity == "MEDIUM":
            score += 3

        else:
            score += 1

    return score