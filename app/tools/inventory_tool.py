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