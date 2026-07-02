from fastapi import FastAPI

from app.core.database import Base, SessionLocal, engine
from app.core.seed import seed_products
from app.models.product import Product
from app.models.sale import Sale
from app.api.chat import router as chat_router
from app.api.inventory import router as inventory_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Seed demo data
db = SessionLocal()
seed_products(db)
db.close()

app = FastAPI(
    title="AI Business Operations Agent",
    description="AI COO for SMEs",
    version="1.0.0",
)

app.include_router(chat_router)
app.include_router(inventory_router)

@app.get("/")
def root():
    return {"message": "AI Business Operations Agent is running 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}