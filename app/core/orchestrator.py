from app.core.llm import ask_gemini
from app.core.tool_registry import TOOL_REGISTRY


class Orchestrator:
    def __init__(self):
        self.tools = TOOL_REGISTRY

    def route(self, user_message: str):
        prompt = f"""
You are an AI COO.

Available tools:
{list(self.tools.keys())}

Your job is to choose ONLY ONE tool.

Rules:

If the request is about:
- inventory
- stock
- products
- quantity
- warehouse
- low stock
- high stock

Reply ONLY:
inventory

If the request is about:
- sales
- analytics
- best selling product
- business performance
- sales report

Reply ONLY:
analytics

If the request is about:
- revenue
- profit
- expense
- finance
- financial
- profit margin
- income

Reply ONLY:
finance

If the request is about:
- reorder
- restock
- procurement
- supplier
- purchase order
- generate purchase order
- approve purchase order
- reject purchase order
- pending purchase orders
- vendor
- buying inventory

Reply ONLY:
procurement

Otherwise reply ONLY:
llm

User:
{user_message}
"""

        tool = ask_gemini(prompt).strip().lower()

        # Remove markdown/code block formatting if Gemini adds it
        tool = tool.replace("```", "").replace("`", "").strip()

        if tool in self.tools:
            return self.tools[tool](user_message)

        return {
            "tool": "llm",
            "response": ask_gemini(user_message),
        }


orchestrator = Orchestrator()