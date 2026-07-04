from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import SessionLocal
from app.models.sale import Sale


def get_financial_summary(db: Session):

    total_revenue = db.query(
        func.sum(Sale.total_amount)
    ).scalar() or 0

    total_profit = db.query(
        func.sum(Sale.profit)
    ).scalar() or 0

    total_expense = db.query(
        func.sum(Sale.cost_price * Sale.quantity)
    ).scalar() or 0

    profit_margin = 0

    if total_revenue > 0:
        profit_margin = round(
            (total_profit / total_revenue) * 100,
            2,
        )

    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "total_profit": total_profit,
        "profit_margin": profit_margin,
    }


def finance_tool(user_message: str):

    db = SessionLocal()

    try:

        summary = get_financial_summary(db)

        recommendation = "Business is financially healthy."

        if summary["profit_margin"] < 10:
            recommendation = (
                "Profit margin is low. Review pricing and reduce expenses."
            )

        elif summary["profit_margin"] < 20:
            recommendation = (
                "Profit margin is moderate. Monitor costs closely."
            )

        message = user_message.lower()

        action = "financial_health"

        if "profit margin" in message:
            action = "profit_margin"

        elif "expense" in message:
            action = "expense_analysis"

        elif "profit" in message:
            action = "profit_analysis"

        elif "revenue" in message:
            action = "revenue_analysis"

        return {
            "tool": "finance",
            "action": action,
            "summary": (
                f"Revenue: ₹{summary['total_revenue']:.2f}, "
                f"Profit: ₹{summary['total_profit']:.2f}, "
                f"Margin: {summary['profit_margin']}%"
            ),
            "metrics": {
                "total_revenue": summary["total_revenue"],
                "total_expense": summary["total_expense"],
                "total_profit": summary["total_profit"],
                "profit_margin": summary["profit_margin"],
            },
            "recommendation": recommendation,
        }

    finally:
        db.close()