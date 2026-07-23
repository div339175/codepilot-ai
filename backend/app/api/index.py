from pathlib import Path

from fastapi import APIRouter, HTTPException
from app.schemas.index import IndexRequest
from app.core.index_builder import build_index

router = APIRouter(
    prefix="/index",
    tags=["Index"]
)

@router.post("/")
def create_index(request: IndexRequest):

    repo_path = Path("repos") / request.repository

    if not repo_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    build_index(repo_path)

    return {
        "message": f"Index built successfully for '{request.repository}'"
    }