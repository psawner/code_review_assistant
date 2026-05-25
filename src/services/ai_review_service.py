import json
import re

from langchain_core.prompts import ChatPromptTemplate

from src.model.llm import get_model

llm = get_model()


def analyze_code(diff):

    prompt = ChatPromptTemplate.from_template("""
You are a senior software engineer reviewing a pull request.

Analyze ONLY the changed code diff.

Focus ONLY on:
1. Security vulnerabilities
2. Performance issues
3. Logical bugs
4. Code maintainability concerns

Rules:
- Ignore formatting/style issues
- Avoid false positives
- Be concise
- Report only meaningful engineering concerns

Code Diff:
{diff}

Return ONLY valid JSON.

Expected JSON format:

{{
  "security": [
    {{
      "issue": "",
      "severity": "LOW/MEDIUM/HIGH",
      "line": 1,
      "explanation": "",
      "suggestion": ""
    }}
  ],

  "performance": [],

  "bugs": [],

  "code_smells": []
}}

If no issues exist, return empty arrays.

DO NOT add explanations outside JSON.
DO NOT use markdown.
DO NOT write ```json.
Return RAW JSON only.
""")

    chain = prompt | llm

    response = chain.invoke({
        "diff": diff
    })

    content = response.content.strip()

    try:

        # Extract JSON safely
        match = re.search(r'\{.*\}', content, re.DOTALL)

        if not match:
            raise ValueError("No JSON object found")

        json_content = match.group()

        parsed = json.loads(json_content)

        # Ensure required keys exist
        return {
            "security": parsed.get("security", []),
            "performance": parsed.get("performance", []),
            "bugs": parsed.get("bugs", []),
            "code_smells": parsed.get("code_smells", [])
        }

    except Exception as e:

        print("\nJSON Parsing Error\n")
        print(e)

        print("\nRaw Response:\n")
        print(content)

        return {
            "security": [],
            "performance": [],
            "bugs": [],
            "code_smells": []
        }