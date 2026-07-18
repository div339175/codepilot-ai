from pathlib import Path
from fastapi import APIRouter, HTTPException

from app.schemas.parser import ParserRequest
from app.core.parser import parse_repository

router = APIRouter(prefix="/parser", tags=["Parser"])


@router.post("/parse")
def parse(request: ParserRequest):

    repo_path = Path("repos") / request.repository

    if not repo_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    metadata = parse_repository(repo_path)

    return {
        "repository": request.repository,
        "total_files": len(metadata),
        "files": metadata
    }