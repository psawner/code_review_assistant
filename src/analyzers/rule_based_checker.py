import re

def run_rule_based_checks(diff):

    findings = []

    rules = [
        {
            "pattern": r'password\s*=\s*["\'].*["\']',
            "issue": "Hardcoded password detected",
            "severity": "HIGH",
            "suggestion": "Use environment variables"
        },

        {
            "pattern": r'eval\(',
            "issue": "Use of eval() detected",
            "severity": "HIGH",
            "suggestion": "Avoid eval() due to code injection risk"
        },

        {
            "pattern": r'print\(',
            "issue": "Debug print statement found",
            "severity": "LOW",
            "suggestion": "Remove debug print statements"
        },

        {
            "pattern": r'TODO|FIXME',
            "issue": "TODO/FIXME comment found",
            "severity": "LOW",
            "suggestion": "Resolve pending TODO items"
        }
    ]

    lines = diff.split("\n")

    for line_number, line in enumerate(lines, start=1):

        for rule in rules:

            if re.search(rule["pattern"], line):

                findings.append({
                    "issue": rule["issue"],
                    "severity": rule["severity"],
                    "line": line_number,
                    "explanation": line.strip(),
                    "suggestion": rule["suggestion"]
                })

    return findings