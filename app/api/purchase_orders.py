from fastapi import APIRouter
from app.core.database import SessionLocal
from app.models.purchase_order import PurchaseOrder

router = APIRouter(
    prefix="/purchase-orders",
    tags=["Purchase Orders"],
)


@router.get("/")
def get_purchase_orders():

    db = SessionLocal()

    try:

        orders = (
            db.query(PurchaseOrder)
            .order_by(PurchaseOrder.created_at.desc())
            .all()
        )

        return [
            {
                "id": o.id,
                "product_name": o.product_name,
                "supplier": o.supplier,
                "quantity": o.quantity,
                "estimated_cost": o.estimated_cost,
                "status": o.status,
            }
            for o in orders
        ]

    finally:
        db.close()


@router.post("/{order_id}/approve")
def approve_order(order_id: int):

    db = SessionLocal()

    try:

        order = (
            db.query(PurchaseOrder)
            .filter(PurchaseOrder.id == order_id)
            .first()
        )

        if order is None:
            return {
                "success": False,
                "message": "Order not found",
            }

        order.status = "APPROVED"

        db.commit()

        return {
            "success": True,
            "message": "Purchase Order Approved",
        }

    finally:
        db.close()


@router.post("/{order_id}/reject")
def reject_order(order_id: int):

    db = SessionLocal()

    try:

        order = (
            db.query(PurchaseOrder)
            .filter(PurchaseOrder.id == order_id)
            .first()
        )

        if order is None:
            return {
                "success": False,
                "message": "Order not found",
            }

        order.status = "REJECTED"

        db.commit()

        return {
            "success": True,
            "message": "Purchase Order Rejected",
        }

    finally:
        db.close()