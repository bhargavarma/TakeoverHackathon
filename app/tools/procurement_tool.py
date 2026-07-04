from sqlalchemy.orm import Session
from sqlalchemy import func
from app.services.email_service import send_email
from app.core.database import SessionLocal
from app.data.suppliers import SUPPLIERS

from app.models.product import Product
from app.models.sale import Sale
from app.models.purchase_order import PurchaseOrder


# ----------------------------------------------------
# PRODUCT HELPERS
# ----------------------------------------------------

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


# ----------------------------------------------------
# SALES FORECASTING
# ----------------------------------------------------

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
        avg_daily_sales * 3,
    )

    qty = target_stock - product.stock

    if qty < 0:
        qty = 0

    return ((qty + 9) // 10) * 10


# ----------------------------------------------------
# SUPPLIER COMPARISON
# ----------------------------------------------------

def get_supplier_comparison(product_name: str):

    suppliers = SUPPLIERS.get(product_name)

    if not suppliers:
        return []

    comparison = []

    for supplier in suppliers:

        score = (
            supplier["rating"] * 25
            - supplier["price"] * 0.35
            - supplier["delivery_days"] * 10
        )

        comparison.append(
            {
                "name": supplier["name"],
                "price": supplier["price"],
                "delivery_days": supplier["delivery_days"],
                "rating": supplier["rating"],
                "score": round(score, 2),
            }
        )

    comparison.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    return comparison


def get_best_supplier(product_name: str):

    comparison = get_supplier_comparison(product_name)

    if not comparison:
        return None

    return comparison[0]


# ----------------------------------------------------
# PURCHASE ORDER GENERATION
# ----------------------------------------------------

def generate_purchase_order(
    db: Session,
    product_name: str,
):

    product = get_product(db, product_name)

    if not product:
        return None

    if pending_order_exists(db, product.name):
        return {
            "status": "already_pending",
            "product": product.name,
        }

    avg_daily_sales = calculate_average_daily_sales(
        db,
        product.id,
    )

    recommended_qty = calculate_recommended_quantity(
        product,
        avg_daily_sales,
    )

    comparison = get_supplier_comparison(product.name)

    if not comparison:
        return None

    supplier = comparison[0]

    estimated_cost = (
        recommended_qty
        * supplier["price"]
    )

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

        "current_stock": product.stock,

        "minimum_stock": product.minimum_stock,

        "average_daily_sales": avg_daily_sales,

        "recommended_quantity": recommended_qty,

        "supplier": supplier["name"],

        "price_per_unit": supplier["price"],

        "estimated_cost": estimated_cost,

        "delivery_days": supplier["delivery_days"],

        "supplier_comparison": comparison,

        "status": order.status,
    }



# ----------------------------------------------------
# DUPLICATE PURCHASE ORDER CHECK
# ----------------------------------------------------

def pending_order_exists(db: Session, product_name: str):
    return (
        db.query(PurchaseOrder)
        .filter(
            func.lower(PurchaseOrder.product_name) == product_name.lower(),
            PurchaseOrder.status == "PENDING",
        )
        .first()
        is not None
    )

# ----------------------------------------------------
# APPROVAL
# ----------------------------------------------------

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

# ----------------------------------------------------
# PROCUREMENT AGENT
# ----------------------------------------------------

def procurement_tool(user_message: str):

    db = SessionLocal()

    try:

        message = user_message.lower()

        # ------------------------------------------------
        # APPROVE PURCHASE ORDER
        # ------------------------------------------------

        if "approve" in message:

            order = approve_purchase_order(db)

            if order is None:
                return {
                    "tool": "procurement",
                    "status": "no_pending_orders",
                    "message": "No purchase orders are waiting for approval.",
                }
            send_email(
                subject="✅ Purchase Order Approved",
                body=f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PURCHASE ORDER APPROVED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Good Afternoon,

The following purchase order has been
approved successfully.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{order.product_name}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏢 SUPPLIER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{order.supplier}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 ORDER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quantity          {order.quantity}

Estimated Cost    ₹{order.estimated_cost}

Status            APPROVED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The procurement process can now proceed
with supplier fulfillment.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated automatically by AI COO.
"""
            )
            return {
                "tool": "procurement",
                "action": "purchase_order_approved",
                "purchase_order": {
                    "id": order.id,
                    "product": order.product_name,
                    "supplier": order.supplier,
                    "quantity": order.quantity,
                    "estimated_cost": order.estimated_cost,
                    "status": order.status,
                },
            }

        # ------------------------------------------------
        # REJECT PURCHASE ORDER
        # ------------------------------------------------

        if "reject" in message:

            order = reject_purchase_order(db)

            if order is None:
                return {
                    "tool": "procurement",
                    "status": "no_pending_orders",
                    "message": "No purchase orders are waiting for approval.",
                }

            return {
                "tool": "procurement",
                "action": "purchase_order_rejected",
                "purchase_order": {
                    "id": order.id,
                    "status": order.status,
                },
            }

        # ------------------------------------------------
        # SHOW PENDING ORDERS
        # ------------------------------------------------

        if "pending" in message:

            orders = get_pending_orders(db)

            return {
                "tool": "procurement",
                "action": "pending_orders",
                "count": len(orders),
                "orders": [
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

        # ------------------------------------------------
        # PRODUCT SPECIFIC REQUEST
        # ------------------------------------------------

        for product in db.query(Product).all():

            if product.name.lower() in message:

                recommendation = generate_purchase_order(
                    db,
                    product.name,
                )

                if recommendation is None:
                    return {
                        "tool": "procurement",
                        "status": "failed",
                        "message": "Unable to generate purchase recommendation.",
                    }

                if recommendation.get("status") == "already_pending":
                    return {
                        "tool": "procurement",
                        "action": "already_pending",
                        "message": f"A pending purchase order already exists for {recommendation['product']}.",
                    }

                comparison = recommendation["supplier_comparison"]
                send_email(
                    subject="🛒 Purchase Order Approval Required",
                    body=f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛒 PURCHASE ORDER APPROVAL REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Good Afternoon,

Your AI COO has completed supplier evaluation
and generated a purchase recommendation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{recommendation['product']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏢 RECOMMENDED SUPPLIER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{recommendation['supplier']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 FINANCIAL SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Price / Unit      ₹{recommendation['price_per_unit']}

Quantity          {recommendation['recommended_quantity']}

Estimated Cost    ₹{recommendation['estimated_cost']}

Delivery Time     {recommendation['delivery_days']} day(s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI DECISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current inventory has fallen below the
recommended safety stock level.

Demand forecasting predicts inventory
depletion within the next few days.

Supplier Selection Criteria

✓ Competitive Pricing

✓ Fast Delivery

✓ High Supplier Rating

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTION REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please review and approve this purchase
order from the AI COO Dashboard.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated automatically by AI COO.
"""
                )

                return {
                    "tool": "procurement",
                    "action": "purchase_recommendation",

                    "product": recommendation["product"],

                    "inventory": {
                        "current_stock": recommendation["current_stock"],
                        "minimum_stock": recommendation["minimum_stock"],
                        "average_daily_sales": recommendation["average_daily_sales"],
                    },

                    "recommendation": {
                        "recommended_quantity": recommendation["recommended_quantity"],
                        "recommended_supplier": recommendation["supplier"],
                        "price_per_unit": recommendation["price_per_unit"],
                        "estimated_cost": recommendation["estimated_cost"],
                        "delivery_days": recommendation["delivery_days"],
                        "purchase_order_status": recommendation["status"],
                    },

                    "supplier_comparison": comparison,

                    "next_action": "Waiting for manager approval before placing the purchase order.",
                }

        # ------------------------------------------------
        # AUTO REVIEW
        # ------------------------------------------------

        low_stock_products = get_low_stock_products(db)

        recommendations = []

        for product in low_stock_products:

            recommendation = generate_purchase_order(
                db,
                product.name,
            )

            if recommendation and recommendation.get("status") != "already_pending":

                recommendations.append(
                    {
                        "product": recommendation["product"],
                        "current_stock": recommendation["current_stock"],
                        "minimum_stock": recommendation["minimum_stock"],
                        "recommended_quantity": recommendation["recommended_quantity"],
                        "recommended_supplier": recommendation["supplier"],
                        "estimated_cost": recommendation["estimated_cost"],
                        "supplier_comparison": recommendation["supplier_comparison"],
                        "status": recommendation["status"],
                    }
                )

        if recommendations:

            body = "Daily Procurement Report\n\n"

            for item in recommendations:

                body += f"""
        Product: {item['product']}
        Current Stock: {item['current_stock']}
        Recommended Qty: {item['recommended_quantity']}
        Supplier: {item['recommended_supplier']}
        Estimated Cost: ₹{item['estimated_cost']}

        ------------------------------------
        """

            send_email(
                subject="📦 Daily Procurement Report",
                body=body,
            )        

        return {
            "tool": "procurement",
            "action": "daily_procurement_review",
            "products_requiring_attention": len(recommendations),
            "recommendations": recommendations,
            "next_action": "Purchase orders have been drafted and are waiting for approval.",
        }

    finally:
        db.close()                                