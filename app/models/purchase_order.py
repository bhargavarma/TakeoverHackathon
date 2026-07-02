from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.core.database import Base


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String, nullable=False)

    supplier = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)

    estimated_cost = Column(Float, nullable=False)

    status = Column(String, default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)