from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.schemas.cache import CacheRequest
from app.analyzers.repository_analyzer import RepositoryAnalyzer
from app.core.analysis_cache import AnalysisCache

router = APIRouter(
    prefix="/analysis/cache",
    tags=["Analysis Cache"]
)

analyzer = RepositoryAnalyzer()
cache = AnalysisCache()


@router.post("/")
def build_cache(request: CacheRequest):

    summary = analyzer.generate_summary(request.repository)

    tech_stack = analyzer.detect_tech_stack(request.repository)

    architecture = analyzer.analyze_architecture(request.repository)

    data = {
        "repository": request.repository,
        "summary": summary,
        "tech_stack": tech_stack,
        "architecture": architecture,
        "generated_at": datetime.now().isoformat()
    }

    cache.save(request.repository, data)

    return {
        "message": "Analysis cached successfully."
    }


@router.get("/{repository}")
def get_cache(repository: str):

    data = cache.load(repository)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Cache not found."
        )

    return data


@router.post("/refresh")
def refresh_cache(request: CacheRequest):

    summary = analyzer.generate_summary(request.repository)

    tech_stack = analyzer.detect_tech_stack(request.repository)

    architecture = analyzer.analyze_architecture(request.repository)

    data = {
        "repository": request.repository,
        "summary": summary,
        "tech_stack": tech_stack,
        "architecture": architecture,
        "generated_at": datetime.now().isoformat()
    }

    cache.save(request.repository, data)

    return {
        "message": "Cache refreshed successfully."
    }