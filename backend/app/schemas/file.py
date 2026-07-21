from pydantic import BaseModel
from typing import List, Optional, Literal


class FileMetadata(BaseModel):
    name: str
    path: str
    extension: str
    language: str
    size: int
    content: str
    type: Literal["file", "folder"]
    children: Optional[List["FileMetadata"]] = None