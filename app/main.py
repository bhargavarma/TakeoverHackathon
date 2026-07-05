from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.purchase_orders import router as purchase_router
from app.core.database import Base, SessionLocal, engine
from app.core.seed import seed_products
from app.core.scheduler import scheduler, start_scheduler
from app.api.dashboard import router as dashboard_router
from app.models.purchase_order import PurchaseOrder
from app.models.product import Product
from app.models.sale import Sale
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.inventory import router as inventory_router
from app.models.user import User
from app.api.dashboard import router as dashboard_router
from app.api.procurement import router as procurement_router

# --------------------------------------------------
# Database Setup
# --------------------------------------------------

Base.metadata.create_all(bind=engine)

db = SessionLocal()
seed_products(db)
db.close()


# --------------------------------------------------
# Application Lifespan
# --------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting AI COO Scheduler...")

    start_scheduler()

    yield

    print("Stopping AI COO Scheduler...")

    scheduler.shutdown()


# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(
    title="AI Business Operations Agent",
    description="AI COO for SMEs",
    version="1.0.0",
    lifespan=lifespan,
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Routes
# --------------------------------------------------

app.include_router(chat_router)
app.include_router(inventory_router)
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(procurement_router)
app.include_router(purchase_router)

# --------------------------------------------------
# Health
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI Business Operations Agent is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }