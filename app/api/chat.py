from fastapi import APIRouter

from app.core.orchestrator import orchestrator
from app.models.chat import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(request: ChatRequest):
    return orchestrator.route(request.message)