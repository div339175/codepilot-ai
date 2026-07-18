from pydantic import BaseModel


class SearchAllRequest(BaseModel):

    query: str

    top_k: int = 5