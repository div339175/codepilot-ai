from pydantic import BaseModel


class SearchRequest(BaseModel):
    repository: str
    query: str
    top_k: int = 5