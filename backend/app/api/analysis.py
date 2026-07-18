from fastapi import APIRouter

from app.schemas.analysis import AnalysisRequest
from app.analyzers.repository_analyzer import RepositoryAnalyzer

router = APIRouter(
    prefix="/analysis",
    tags=["Repository Analysis"]
)

analyzer = RepositoryAnalyzer()


@router.post("/")
def analyze(request: AnalysisRequest):

    summary = analyzer.generate_summary(request.repository)

    return {
        "repository": request.repository,
        "summary": summary
    }