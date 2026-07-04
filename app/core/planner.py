import json

from app.core.llm import ask_gemini


def create_execution_plan(user_message: str):

    prompt = f"""
You are an AI COO.

Your ONLY task is to generate an execution plan.

Available agents:

- inventory
- analytics
- finance
- procurement
- notifications

Return ONLY valid JSON.

Example:

{{
    "workflow":"daily_review",
    "steps":[
        "inventory",
        "analytics",
        "finance",
        "procurement",
        "notifications"
    ]
}}

User:

{user_message}
"""

    response = ask_gemini(prompt)

    response = (
        response.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        plan = json.loads(response)

        if "workflow" not in plan:
            plan["workflow"] = "daily_review"

        if "steps" not in plan:
            plan["steps"] = []

        return plan

    except Exception:

        print("\nPlanner Error\n")
        print(response)

        return {
            "workflow": "daily_review",
            "steps": [
                "inventory",
                "analytics",
                "finance",
                "procurement",
                "notifications",
            ],
        }