from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.repository_service import RepositoryService
from app.services.agent_service import AgentService

agent = AgentService()

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)

service = RepositoryService()


@router.post("/")
def chat(request: ChatRequest):

    result = service.ask(
    repository=request.repository,
    question=request.question
    )

    return {
        "repository": request.repository,
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }

from pydantic import BaseModel


class AgentRequest(BaseModel):

    repository: str

    current_file: str | None = None

    current_content: str

    message: str

@router.post("/agent")
def agent_chat(request: AgentRequest):

    return agent.ask(
        request.repository,
        request.current_file,
        request.current_content,
        request.message,
    )