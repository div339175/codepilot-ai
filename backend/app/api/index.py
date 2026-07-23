from pathlib import Path

from fastapi import APIRouter, HTTPException, BackgroundTasks

from app.schemas.index import IndexRequest
from app.core.index_builder import build_index
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/index",
    tags=["Index"]
)

analysis_service = AnalysisService()


def process_repository(repository: str):

    repo_path = Path("repos") / repository

    # Step 1: Build FAISS index
    build_index(repo_path)

    # Step 2: Automatically generate analysis
    analysis_service.generate(repository)


@router.post("/")
def create_index(
    request: IndexRequest,
    background_tasks: BackgroundTasks
):

    repo_path = Path("repos") / request.repository

    if not repo_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    background_tasks.add_task(
        process_repository,
        request.repository
    )

    return {
        "message": f"Started processing '{request.repository}'"
    }