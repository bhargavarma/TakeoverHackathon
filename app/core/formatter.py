import json

from app.core.llm import ask_gemini


def format_agent_response(agent_name: str, data: dict):

    prompt = f"""
You are an AI Chief Operating Officer.

An internal business agent has completed its work.

Agent:
{agent_name}

Structured Output:
{json.dumps(data, indent=2)}

Your job:

1. Summarize what happened.

2. Explain WHY it matters.

3. Mention any business risks.

4. Mention any recommendations.

5. If approval is required,
clearly say the purchase order is waiting for approval.

Never mention JSON.

Write like an experienced COO.

Keep the answer below 200 words.
"""

    return ask_gemini(prompt)