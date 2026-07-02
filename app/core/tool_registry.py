from app.tools.inventory_tool import inventory_tool
from app.tools.analytics_tool import analytics_tool
from app.tools.procurement_tool import procurement_tool
from app.tools.finance_tool import finance_tool
from app.tools.notification_tool import notification_tool

TOOL_REGISTRY = {
    "inventory": inventory_tool,
    "analytics": analytics_tool,
    "procurement": procurement_tool,
    "finance": finance_tool,
    "notification": notification_tool,
}