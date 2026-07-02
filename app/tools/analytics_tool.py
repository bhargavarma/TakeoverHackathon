from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.sale import Sale
from app.models.product import Product


def get_total_revenue(db: Session):
    revenue = db.query(func.sum(Sale.total_amount)).scalar()
    return revenue or 0


def get_total_profit(db: Session):
    profit = db.query(func.sum(Sale.profit)).scalar()
    return profit or 0


def get_total_orders(db: Session):
    return db.query(Sale).count()


def get_best_selling_product(db: Session):
    result = (
        db.query(
            Product.name,
            func.sum(Sale.quantity).label("total_sold")
        )
        .join(Sale, Product.id == Sale.product_id)
        .group_by(Product.id)
        .order_by(func.sum(Sale.quantity).desc())
        .first()
    )

    if result:
        return {
            "product": result.name,
            "quantity_sold": result.total_sold,
        }

    return None


def analytics_tool(user_message: str):
    db = SessionLocal()

    try:
        message = user_message.lower()

        # Revenue
        if "revenue" in message:
            return {
                "tool": "analytics",
                "total_revenue": get_total_revenue(db)
            }

        # Profit
        elif "profit" in message:
            return {
                "tool": "analytics",
                "total_profit": get_total_profit(db)
            }

        # Orders
        elif "order" in message:
            return {
                "tool": "analytics",
                "total_orders": get_total_orders(db)
            }

        # Best Selling Product
        elif (
            "best" in message
            or "top" in message
            or "selling" in message
            or "highest selling" in message
        ):
            return {
                "tool": "analytics",
                "best_selling_product": get_best_selling_product(db)
            }

        # Business Summary
        elif (
            "summary" in message
            or "overview" in message
            or "performance" in message
            or "analytics" in message
        ):
            return {
                "tool": "analytics",
                "summary": {
                    "total_revenue": get_total_revenue(db),
                    "total_profit": get_total_profit(db),
                    "total_orders": get_total_orders(db),
                    "best_selling_product": get_best_selling_product(db),
                },
            }

        # Default
        return {
            "tool": "analytics",
            "message": (
                "I can help with revenue, profit, orders, "
                "best selling product, or a business summary."
            ),
        }

    finally:
        db.close()