from pydantic import BaseModel


class CompareRequest(BaseModel):
    repository_1: str
    repository_2: str