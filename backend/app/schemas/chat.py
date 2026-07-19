from pydantic import BaseModel


class ChatRequest(BaseModel):
    repository: str
    question: str


class Source(BaseModel):
    file: str
    score: float


class ChatResponse(BaseModel):
    repository: str
    question: str
    answer: str
    sources: list[Source]