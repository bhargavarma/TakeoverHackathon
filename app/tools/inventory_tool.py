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

        # Decide which products to fetch
        if "low" in message:
            products = get_low_stock_products(db)

        elif "high" in message:
            products = get_high_stock_products(db)

        else:
            products = get_all_products(db)

        return {
            "tool": "inventory",
            "result": [
                {
                    "name": p.name,
                    "stock": p.stock,
                    "minimum_stock": p.minimum_stock,
                    "cost_price": p.cost_price,
                    "selling_price": p.selling_price,
                    "supplier": p.supplier,
                }
                for p in products
            ],
        }

    finally:
        db.close()