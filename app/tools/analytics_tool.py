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


def get_slow_moving_products(db: Session):

    results = (
        db.query(
            Product.name,
            func.sum(Sale.quantity).label("total_sold")
        )
        .join(Sale, Product.id == Sale.product_id)
        .group_by(Product.id)
        .order_by(func.sum(Sale.quantity).asc())
        .limit(3)
        .all()
    )

    return [
        {
            "product": r.name,
            "quantity_sold": r.total_sold,
        }
        for r in results
    ]


def analytics_tool(user_message: str):

    db = SessionLocal()

    try:

        revenue = get_total_revenue(db)
        profit = get_total_profit(db)
        orders = get_total_orders(db)
        best = get_best_selling_product(db)
        slow = get_slow_moving_products(db)

        action = "business_analytics"

        message = user_message.lower()

        if "revenue" in message:
            action = "revenue_analysis"

        elif "profit" in message:
            action = "profit_analysis"

        elif "order" in message:
            action = "order_analysis"

        elif (
            "best" in message
            or "top" in message
            or "selling" in message
        ):
            action = "sales_analysis"

        summary = (
            f"Business has processed {orders} orders, "
            f"generated ₹{revenue:.2f} revenue "
            f"with ₹{profit:.2f} profit."
        )

        recommendations = []

        if best:
            recommendations.append(
                f"Maintain inventory of {best['product']}."
            )

        if slow:
            recommendations.append(
                "Consider discounts for slow-moving products."
            )

        return {
            "tool": "analytics",
            "action": action,
            "summary": summary,
            "metrics": {
                "total_revenue": revenue,
                "total_profit": profit,
                "total_orders": orders,
            },
            "best_selling_product": best,
            "slow_moving_products": slow,
            "recommendations": recommendations,
        }

    finally:
        db.close()