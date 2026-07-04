from app.core.planner import create_execution_plan
from app.core.formatter import format_agent_response

from app.tools.inventory_tool import inventory_tool
from app.tools.analytics_tool import analytics_tool
from app.tools.finance_tool import finance_tool
from app.tools.procurement_tool import procurement_tool
from app.tools.notification_tool import notification_tool


class WorkflowEngine:

    def execute(self, user_message: str):

        plan = create_execution_plan(user_message)

        results = {}

        for step in plan.get("steps", []):

            if step == "inventory":
                results["inventory"] = inventory_tool(user_message)

            elif step == "analytics":
                results["analytics"] = analytics_tool(user_message)

            elif step == "finance":
                results["finance"] = finance_tool(user_message)

            elif step == "procurement":
                results["procurement"] = procurement_tool(user_message)

            elif step == "notifications":
                results["notifications"] = notification_tool(user_message)

        summary = format_agent_response(
            "Business Operations Workflow",
            results,
        )

        return {
            "workflow": plan.get("workflow"),
            "summary": summary,
            "results": results,
        }


workflow_engine = WorkflowEngine()