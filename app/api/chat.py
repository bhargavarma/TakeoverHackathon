from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.core.llm import ask_gemini

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(request: ChatRequest):
    response = ask_gemini(request.message)

    return {
        "response": response
    }