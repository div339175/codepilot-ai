from pathlib import Path

from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.analyzers.repository_analyzer import RepositoryAnalyzer
from app.core.analysis_cache import AnalysisCache
from app.schemas.index import IndexRequest
from app.core.index_builder import build_index

router = APIRouter(
    prefix="/index",
    tags=["Index"]
)

analyzer = RepositoryAnalyzer()
cache = AnalysisCache()

@router.post("/")
def create_index(request: IndexRequest):

    repo_path = Path("repos") / request.repository

    if not repo_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    build_index(repo_path)
    summary = analyzer.generate_summary(request.repository)
    tech_stack = analyzer.detect_tech_stack(request.repository)
    architecture = analyzer.analyze_architecture(request.repository)

    cache.save(
        request.repository,
        {
            "repository": request.repository,
            "summary": summary,
            "tech_stack": tech_stack,
            "architecture": architecture,
            "generated_at": datetime.now().isoformat()
        }
    )

    return {
        "message": f"Index built successfully for '{request.repository}'"
    }