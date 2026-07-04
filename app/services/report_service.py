from datetime import datetime


def generate_daily_report(
    inventory,
    analytics,
    finance,
    procurement,
):

    inventory_summary = inventory.get(
        "summary",
        "Inventory review completed."
    )

    business_summary = analytics.get(
        "summary",
        "Business analytics completed."
    )

    finance_metrics = finance.get("metrics", {})

    procurement_count = len(
        procurement.get("recommendations", [])
    )

    if procurement_count > 0:

        procurement_summary = (
            f"{procurement_count} purchase recommendation(s) "
            "generated and waiting for approval."
        )

        ai_recommendation = (
            "Approve today's purchase orders to avoid "
            "future stock shortages."
        )

    else:

        procurement_summary = (
            "No procurement action required."
        )

        ai_recommendation = (
            "Inventory is healthy. "
            "No purchase orders were required today."
        )

    report = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI COO DAILY BUSINESS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Good Morning,

Your AI COO has successfully completed today's
business operations review.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 DATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{datetime.now().strftime("%d %B %Y")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 TODAY'S AI DECISIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Reviewed Inventory

✅ Analysed Business Performance

✅ Reviewed Financial Health

{"✅ Generated Purchase Orders" if procurement_count > 0 else "✅ Procurement Review Completed"}

✅ Executive Report Generated

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 FINANCIAL OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Revenue

₹{finance_metrics.get("total_revenue", 0):.2f}

Profit

₹{finance_metrics.get("total_profit", 0):.2f}

Profit Margin

{finance_metrics.get("profit_margin", 0)}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 INVENTORY STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{inventory_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 BUSINESS ANALYTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{business_summary}

Best Selling Product

{analytics.get("best_selling_product", {}).get("product", "N/A")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛒 PROCUREMENT STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{procurement_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 AI RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{ai_recommendation}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated automatically by AI COO.

No manual intervention was required
unless purchase approval is pending.
"""

    return report