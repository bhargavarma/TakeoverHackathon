from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Procurement"],
)

@router.get("/purchase-orders")
def purchase_orders():
    return [
        {
            "id": 1,
            "item": "Milk",
            "status": "Pending Approval",
        },
        {
            "id": 2,
            "item": "Coffee",
            "status": "Pending Approval",
        },
        {
            "id": 3,
            "item": "Sugar",
            "status": "Pending Approval",
        },
    ]

@router.post("/review/run")
def run_review():
    return {
        "message": "AI Daily Review completed successfully."
    }