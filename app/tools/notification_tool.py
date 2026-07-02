from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.product import Product
from app.models.purchase_order import PurchaseOrder


def get_low_stock_alerts(db: Session):
    products = (
        db.query(Product)
        .filter(Product.stock <= Product.minimum_stock)
        .all()
    )

    return [
        {
            "type": "LOW_STOCK",
            "product": p.name,
            "current_stock": p.stock,
            "minimum_stock": p.minimum_stock,
        }
        for p in products
    ]


def get_pending_purchase_orders(db: Session):
    orders = (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.status == "PENDING")
        .all()
    )

    return [
        {
            "type": "PURCHASE_APPROVAL",
            "order_id": o.id,
            "product": o.product_name,
            "supplier": o.supplier,
            "quantity": o.quantity,
            "estimated_cost": o.estimated_cost,
        }
        for o in orders
    ]


def notification_tool(user_message: str):

    db = SessionLocal()

    try:

        message = user_message.lower()

        low_stock = get_low_stock_alerts(db)

        pending_orders = get_pending_purchase_orders(db)

        if "low" in message:

            return {
                "tool": "notification",
                "alerts": low_stock,
            }

        if "pending" in message or "approval" in message:

            return {
                "tool": "notification",
                "pending_orders": pending_orders,
            }

        return {
            "tool": "notification",
            "notifications": {
                "low_stock_alerts": low_stock,
                "pending_purchase_orders": pending_orders,
            },
        }

    finally:
        db.close()