from sqlalchemy.orm import Session

from app.models.product import Product


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


def update_stock(db: Session, product_name: str, new_stock: int):
    product = get_product(db, product_name)

    if product is None:
        return None

    product.stock = new_stock
    db.commit()
    db.refresh(product)

    return product
from app.core.database import SessionLocal


def inventory_tool(user_message: str):
    db = SessionLocal()

    try:
        message = user_message.lower()

        if "low" in message:
            products = get_low_stock_products(db)

            return {
                "tool": "inventory",
                "result": [
                    {
                        "name": p.name,
                        "stock": p.stock,
                        "minimum_stock": p.minimum_stock,
                    }
                    for p in products
                ],
            }

        products = get_all_products(db)

        return {
            "tool": "inventory",
            "result": [
                {
                    "name": p.name,
                    "stock": p.stock,
                    "price": p.price,
                }
                for p in products
            ],
        }

    finally:
        db.close()