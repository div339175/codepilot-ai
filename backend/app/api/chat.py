from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.repository_service import RepositoryService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)

service = RepositoryService()


@router.post("/")
def chat(request: ChatRequest):

    answer = service.ask(request.question)

    return {
        "question": request.question,
        "answer": answer
    }