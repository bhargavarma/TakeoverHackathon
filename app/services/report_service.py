from datetime import datetime


def generate_daily_report(
    inventory,
    analytics,
    finance,
    procurement,
):
    report = f"""
Good Morning,

Your AI COO has completed today's operational review.

==================================================
📊 DAILY BUSINESS OPERATIONS REPORT
==================================================

Date:
{datetime.now().strftime("%d %B %Y")}

==================================================
💰 FINANCIAL OVERVIEW
==================================================

Revenue
₹{finance["metrics"]["total_revenue"]:.2f}

Profit
₹{finance["metrics"]["total_profit"]:.2f}

Profit Margin
{finance["metrics"]["profit_margin"]}%

==================================================
📦 INVENTORY STATUS
==================================================

{inventory["summary"]}

==================================================
📈 BUSINESS ANALYTICS
==================================================

Orders Processed
{analytics["metrics"]["total_orders"]}

Best Selling Product

{analytics["best_selling_product"]["product"]}

==================================================
🛒 PROCUREMENT
==================================================

{len(procurement.get("recommendations", []))}
Purchase Recommendation(s) Generated

==================================================
🤖 AI RECOMMENDATION
==================================================

Review today's purchase recommendations.

Approve urgent purchase orders to
avoid stock shortages.

==================================================

Generated automatically by AI COO.
"""

    return report