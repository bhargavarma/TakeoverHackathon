from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import SessionLocal
from app.models.sale import Sale


def get_financial_summary(db: Session):

    total_revenue = db.query(func.sum(Sale.total_amount)).scalar() or 0

    total_profit = db.query(func.sum(Sale.profit)).scalar() or 0

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

        message = user_message.lower()

        if "profit margin" in message:
            return {
                "tool": "finance",
                "profit_margin": summary["profit_margin"],
            }

        if "expense" in message:
            return {
                "tool": "finance",
                "total_expense": summary["total_expense"],
            }

        if "profit" in message:
            return {
                "tool": "finance",
                "total_profit": summary["total_profit"],
            }

        if "revenue" in message:
            return {
                "tool": "finance",
                "total_revenue": summary["total_revenue"],
            }

        return {
            "tool": "finance",
            **summary
        }

    finally:
        db.close()