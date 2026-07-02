from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import SessionLocal
from app.data.suppliers import SUPPLIERS

from app.models.product import Product
from app.models.sale import Sale
from app.models.purchase_order import PurchaseOrder


def get_low_stock_products(db: Session):
    return (
        db.query(Product)
        .filter(Product.stock <= Product.minimum_stock)
        .all()
    )


def get_product(db: Session, product_name: str):
    return (
        db.query(Product)
        .filter(func.lower(Product.name) == product_name.lower())
        .first()
    )


def calculate_average_daily_sales(db: Session, product_id: int):
    sales = (
        db.query(func.sum(Sale.quantity))
        .filter(Sale.product_id == product_id)
        .scalar()
    )

    if not sales:
        return 0

    return max(1, round(sales / 7))


def calculate_recommended_quantity(product, avg_daily_sales):
    target_stock = max(
        product.minimum_stock * 2,
        avg_daily_sales * 3
    )

    qty = target_stock - product.stock

    if qty < 0:
        qty = 0

    return ((qty + 9) // 10) * 10


def get_best_supplier(product_name: str):

    suppliers = SUPPLIERS.get(product_name)

    if not suppliers:
        return None

    def score(s):

        price_score = s["price"]

        delivery_score = s["delivery_days"] * 5

        rating_score = (5 - s["rating"]) * 10

        return price_score + delivery_score + rating_score

    return min(suppliers, key=score)
def generate_purchase_order(db: Session, product_name: str):

    product = get_product(db, product_name)

    if not product:
        return None

    avg_daily_sales = calculate_average_daily_sales(db, product.id)

    recommended_qty = calculate_recommended_quantity(
        product,
        avg_daily_sales,
    )

    supplier = get_best_supplier(product.name)

    if supplier is None:
        return None

    estimated_cost = recommended_qty * supplier["price"]

    order = PurchaseOrder(
        product_name=product.name,
        supplier=supplier["name"],
        quantity=recommended_qty,
        estimated_cost=estimated_cost,
        status="PENDING",
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "order_id": order.id,
        "product": product.name,
        "recommended_quantity": recommended_qty,
        "supplier": supplier["name"],
        "price_per_unit": supplier["price"],
        "estimated_cost": estimated_cost,
        "delivery_days": supplier["delivery_days"],
        "status": order.status,
    }


def approve_purchase_order(db: Session):

    order = (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.status == "PENDING")
        .order_by(PurchaseOrder.created_at.desc())
        .first()
    )

    if order is None:
        return None

    order.status = "APPROVED"

    db.commit()
    db.refresh(order)

    return order


def reject_purchase_order(db: Session):

    order = (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.status == "PENDING")
        .order_by(PurchaseOrder.created_at.desc())
        .first()
    )

    if order is None:
        return None

    order.status = "REJECTED"

    db.commit()
    db.refresh(order)

    return order


def get_pending_orders(db: Session):

    return (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.status == "PENDING")
        .all()
    )
def procurement_tool(user_message: str):
    db = SessionLocal()

    try:
        message = user_message.lower()

        # Approve latest purchase order
        if "approve" in message:

            order = approve_purchase_order(db)

            if order is None:
                return {
                    "tool": "procurement",
                    "message": "There are no pending purchase orders."
                }

            return {
                "tool": "procurement",
                "message": "Purchase order approved successfully.",
                "purchase_order": {
                    "id": order.id,
                    "product": order.product_name,
                    "supplier": order.supplier,
                    "quantity": order.quantity,
                    "estimated_cost": order.estimated_cost,
                    "status": order.status,
                },
            }

        # Reject latest purchase order
        if "reject" in message:

            order = reject_purchase_order(db)

            if order is None:
                return {
                    "tool": "procurement",
                    "message": "There are no pending purchase orders."
                }

            return {
                "tool": "procurement",
                "message": "Purchase order rejected.",
                "purchase_order": {
                    "id": order.id,
                    "status": order.status,
                },
            }

        # Show pending purchase orders
        if "pending" in message:

            orders = get_pending_orders(db)

            return {
                "tool": "procurement",
                "pending_orders": [
                    {
                        "id": o.id,
                        "product": o.product_name,
                        "supplier": o.supplier,
                        "quantity": o.quantity,
                        "estimated_cost": o.estimated_cost,
                        "status": o.status,
                    }
                    for o in orders
                ],
            }

        # Recommendation / Generate PO
        for product in db.query(Product).all():

            if product.name.lower() in message:

                recommendation = generate_purchase_order(db, product.name)

                if recommendation is None:
                    return {
                        "tool": "procurement",
                        "message": "Unable to generate recommendation."
                    }

                return {
                    "tool": "procurement",
                    "recommendation": {
                        "product": recommendation["product"],
                        "reason": (
                            "Current stock is below the recommended level "
                            "based on demand forecasting."
                        ),
                        "recommended_quantity": recommendation["recommended_quantity"],
                        "supplier": recommendation["supplier"],
                        "price_per_unit": recommendation["price_per_unit"],
                        "estimated_cost": recommendation["estimated_cost"],
                        "delivery_days": recommendation["delivery_days"],
                        "status": recommendation["status"],
                    },
                }

        # Products needing reorder
        products = get_low_stock_products(db)

        recommendations = []

        for product in products:

            recommendation = generate_purchase_order(db, product.name)

            if recommendation:

                recommendations.append(recommendation)

        return {
            "tool": "procurement",
            "recommendations": recommendations,
        }

    finally:
        db.close()