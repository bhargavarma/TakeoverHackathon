from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.product import Product
from app.models.sale import Sale


def seed_products(db: Session):
    """Insert demo products and demo sales if tables are empty."""

    # -----------------------------
    # Seed Products
    # -----------------------------
    if not db.query(Product).first():

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

    # -----------------------------
    # Seed Sales
    # -----------------------------
    if not db.query(Sale).first():

        products = db.query(Product).all()

        sales = [
            Sale(
                product_id=products[0].id,
                quantity=20,
                cost_price=45,
                selling_price=55,
                total_amount=20 * 55,
                profit=20 * (55 - 45),
                created_at=datetime.now() - timedelta(days=1),
            ),
            Sale(
                product_id=products[1].id,
                quantity=35,
                cost_price=20,
                selling_price=30,
                total_amount=35 * 30,
                profit=35 * (30 - 20),
                created_at=datetime.now() - timedelta(days=2),
            ),
            Sale(
                product_id=products[2].id,
                quantity=60,
                cost_price=5,
                selling_price=8,
                total_amount=60 * 8,
                profit=60 * (8 - 5),
                created_at=datetime.now() - timedelta(days=3),
            ),
            Sale(
                product_id=products[3].id,
                quantity=100,
                cost_price=45,
                selling_price=60,
                total_amount=100 * 60,
                profit=100 * (60 - 45),
                created_at=datetime.now() - timedelta(days=4),
            ),
            Sale(
                product_id=products[4].id,
                quantity=25,
                cost_price=35,
                selling_price=50,
                total_amount=25 * 50,
                profit=25 * (50 - 35),
                created_at=datetime.now() - timedelta(days=5),
            ),
        ]

        db.add_all(sales)
        db.commit()