from sqlalchemy.orm import Session

from app.models.product import Product
from app.core.database import SessionLocal


def get_product(db: Session, product_name: str):
    """
    Returns a product by its name.
    """
    return (
        db.query(Product)
        .filter(Product.name == product_name)
        .first()
    )


def get_all_products(db: Session):
    return db.query(Product).all()


def get_low_stock_products(db: Session):
    return (
        db.query(Product)
        .filter(Product.stock <= Product.minimum_stock)
        .all()
    )


def get_high_stock_products(db: Session):
    return (
        db.query(Product)
        .filter(Product.stock > Product.minimum_stock)
        .all()
    )


def update_stock(db: Session, product_name: str, new_stock: int):
    product = get_product(db, product_name)

    if product is None:
        return None

    product.stock = new_stock
    db.commit()
    db.refresh(product)

    return product


def inventory_tool(user_message: str):
    db = SessionLocal()

    try:
        message = user_message.lower()

        if "low" in message:
            products = get_low_stock_products(db)
            action = "low_stock_analysis"

        elif "high" in message:
            products = get_high_stock_products(db)
            action = "high_stock_analysis"

        else:
            products = get_all_products(db)
            action = "inventory_overview"

        inventory = []
        critical_count = 0

        for p in products:

            severity = "Normal"

            if p.stock <= p.minimum_stock:

                if p.stock <= (p.minimum_stock * 0.5):
                    severity = "Critical"
                else:
                    severity = "Low"

                critical_count += 1

            inventory.append(
                {
                    "name": p.name,
                    "current_stock": p.stock,
                    "minimum_stock": p.minimum_stock,
                    "cost_price": p.cost_price,
                    "selling_price": p.selling_price,
                    "supplier": p.supplier,
                    "severity": severity,
                }
            )

        if action == "inventory_overview":
            summary = (
                f"Inventory contains {len(inventory)} products."
            )

        elif action == "low_stock_analysis":
            summary = (
                f"{critical_count} products require replenishment."
            )

        else:
            summary = (
                f"{len(inventory)} products are sufficiently stocked."
            )

        return {
            "tool": "inventory",
            "action": action,
            "summary": summary,
            "products": inventory,
            "next_action": (
                "Generate purchase orders for low stock products."
                if critical_count > 0
                else "No procurement action required."
            ),
        }

    finally:
        db.close()