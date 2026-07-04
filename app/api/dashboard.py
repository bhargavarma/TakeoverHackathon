from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get("/")
def dashboard():

    return {
        "revenue": 124000,
        "profit": 31800,
        "inventory": 184,
        "orders": 96,
        "health": 94,
    }