from pydantic import BaseModel


class FileMetadata(BaseModel):
    name: str
    path: str
    extension: str
    language: str
    size: int
    content: str