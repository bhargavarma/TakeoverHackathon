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

If the user is asking about inventory, stock, products, quantity, low stock or warehouse,
reply with ONLY:

inventory

Otherwise reply with:

llm

User:
{user_message}
"""

        tool = ask_gemini(prompt).strip().lower()

        if tool in self.tools:
            return self.tools[tool](user_message)

        return {
            "tool": "llm",
            "response": ask_gemini(user_message)
        }


orchestrator = Orchestrator()