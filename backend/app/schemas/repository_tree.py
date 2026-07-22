from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Literal


class RepositoryTreeNode(BaseModel):
    name: str
    path: str
    type: Literal["file", "folder"]

    children: List["RepositoryTreeNode"] = Field(default_factory=list)