from app.core.planner import create_execution_plan
from app.core.formatter import format_agent_response
from app.services.report_service import generate_daily_report
from app.services.email_service import send_email

from app.tools.inventory_tool import inventory_tool
from app.tools.analytics_tool import analytics_tool
from app.tools.finance_tool import finance_tool
from app.tools.procurement_tool import procurement_tool
from app.tools.notification_tool import notification_tool


class WorkflowEngine:

    def execute(self, user_message: str):

        plan = create_execution_plan(user_message)

        results = {}

        # ----------------------------
        # Inventory Review (Always First)
        # ----------------------------
        inventory = inventory_tool(user_message)
        results["inventory"] = inventory

        # ----------------------------
        # AI Decision:
        # Does Procurement Need To Run?
        # ----------------------------
        procurement_required = False

        for product in inventory.get("products", []):

            if product.get("severity") in ["Low", "Critical"]:
                procurement_required = True
                break

        # ----------------------------
        # Continue Workflow
        # ----------------------------
        for step in plan.get("steps", []):

            if step == "inventory":
                continue

            elif step == "analytics":
                results["analytics"] = analytics_tool(user_message)

            elif step == "finance":
                results["finance"] = finance_tool(user_message)

            elif step == "procurement":

                if procurement_required:

                    results["procurement"] = procurement_tool(
                        "generate purchase orders"
                    )

                else:

                    results["procurement"] = {
                        "tool": "procurement",
                        "action": "none",
                        "summary": "Inventory is healthy. No purchase orders required.",
                        "recommendations": [],
                    }

            elif step == "notifications":
                results["notifications"] = notification_tool(user_message)

        # ----------------------------
        # AI Executive Summary
        # ----------------------------
        summary = format_agent_response(
            "Business Operations Workflow",
            results,
        )

        # ----------------------------
        # Daily Executive Report Email
        # ----------------------------
        try:

            report = generate_daily_report(
                results.get("inventory", {}),
                results.get("analytics", {}),
                results.get("finance", {}),
                results.get("procurement", {}),
            )

            send_email(
                subject="📊 Daily Business Operations Report | AI COO",
                body=report,
            )

        except Exception as e:

            print("Daily report email failed:", e)

        return {
            "workflow": plan.get("workflow"),
            "summary": summary,
            "results": results,
        }


workflow_engine = WorkflowEngine()