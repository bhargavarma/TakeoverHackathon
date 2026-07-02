from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)
    stock = Column(Integer)
    minimum_stock = Column(Integer)
    cost_price = Column(Float)
    selling_price = Column(Float)
    supplier = Column(String)