from fastapi import APIRouter

from app.core.database import SessionLocal
from app.tools.inventory_tool import get_all_products

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
def get_inventory():
    db = SessionLocal()

    try:
        products = get_all_products(db)

        return [
            {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "stock": product.stock,
                "minimum_stock": product.minimum_stock,
                "supplier": product.supplier,
            }
            for product in products
        ]

    finally:
        db.close()