from fastapi import APIRouter
from sqlalchemy import func

from app.core.database import SessionLocal
from app.models.product import Product
from app.models.purchase_order import PurchaseOrder
from app.models.sale import Sale

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/")
def dashboard():

    db = SessionLocal()

    try:

        revenue = (
            db.query(func.sum(Sale.quantity * Sale.selling_price))
            .scalar()
            or 0
        )

        profit = (
            db.query(
                func.sum(
                    Sale.quantity
                    * (Sale.selling_price - Sale.cost_price)
                )
            )
            .scalar()
            or 0
        )

        inventory = db.query(Product).count()

        orders = (
            db.query(PurchaseOrder)
            .filter(PurchaseOrder.status == "PENDING")
            .count()
        )

        health = 94

        return {
            "revenue": revenue,
            "profit": profit,
            "inventory": inventory,
            "orders": orders,
            "health": health,
        }

    finally:
        db.close()