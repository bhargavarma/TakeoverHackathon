from app.core.llm import ask_gemini
from app.core.tool_registry import TOOL_REGISTRY
from app.core.workflow_engine import workflow_engine


class Orchestrator:

    def __init__(self):
        self.tools = TOOL_REGISTRY

    def route(self, user_message: str):

        prompt = f"""
You are the AI COO of a company.

Your job is to decide whether the user needs:

1. A COMPLETE BUSINESS WORKFLOW

or

2. A SINGLE AGENT

Available Agents:

inventory
analytics
finance
procurement
notification

If the user asks things like:

- daily review
- business review
- business health
- review my business
- run operations
- today's report
- executive summary
- company review
- analyze my business
- review today's business
- perform daily operations

Reply ONLY:

workflow

------------------------------------

If the user asks ONLY about inventory,
reply ONLY:

inventory

If the user asks ONLY about analytics,
reply ONLY:

analytics

If the user asks ONLY about finance,
reply ONLY:

finance

If the user asks ONLY about procurement,
reply ONLY:

procurement

If the user asks ONLY about notifications,
reply ONLY:

notification

Otherwise reply ONLY:

llm

User:

{user_message}
"""

        decision = ask_gemini(prompt).strip().lower()

        decision = (
            decision.replace("```", "")
            .replace("`", "")
            .strip()
        )

        if decision == "workflow":
            return workflow_engine.execute(user_message)

        if decision in self.tools:
            return self.tools[decision](user_message)

        return {
            "tool": "llm",
            "response": ask_gemini(user_message),
        }


orchestrator = Orchestrator()