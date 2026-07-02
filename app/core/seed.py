from sqlalchemy.orm import Session

from app.models.product import Product


def seed_products(db: Session):
    """Insert demo products if the table is empty."""

    if db.query(Product).first():
        return

    products = [
        Product(
            name="Milk",
            category="Dairy",
            stock=15,
            minimum_stock=30,
            cost_price=45,
            selling_price=55,
            supplier="ABC Dairy",
        ),
        Product(
            name="Bread",
            category="Bakery",
            stock=40,
            minimum_stock=20,
            cost_price=20,
            selling_price=30,
            supplier="Fresh Bakers",
        ),
        Product(
            name="Eggs",
            category="Dairy",
            stock=18,
            minimum_stock=25,
            cost_price=5,
            selling_price=8,
            supplier="Farm Fresh",
        ),
        Product(
            name="Rice",
            category="Groceries",
            stock=120,
            minimum_stock=50,
            cost_price=45,
            selling_price=60,
            supplier="Grain India",
        ),
        Product(
            name="Soft Drinks",
            category="Beverages",
            stock=8,
            minimum_stock=20,
            cost_price=35,
            selling_price=50,
            supplier="Cool Drinks Ltd",
        ),
    ]

    db.add_all(products)
    db.commit()