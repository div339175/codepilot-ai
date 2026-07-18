from pydantic import BaseModel


class IndexRequest(BaseModel):
    repository: str