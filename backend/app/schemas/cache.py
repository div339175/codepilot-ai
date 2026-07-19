from pydantic import BaseModel


class CacheRequest(BaseModel):
    repository: str