from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Procurement"],
)


@router.post("/review/run")
def run_review():
    return {
        "success": True,
        "message": "AI Daily Review completed successfully."
    }