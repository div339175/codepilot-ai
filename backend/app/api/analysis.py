from fastapi import APIRouter

from app.schemas.analysis import (
    AnalysisRequest,
    FileAnalysisRequest,
    FolderAnalysisRequest
)
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

@router.post("/file")
def analyze_file(request: FileAnalysisRequest):

    explanation = analyzer.explain_file(
        request.repository,
        request.file_path,
    )

    return {
        "repository": request.repository,
        "file": request.file_path,
        "analysis": explanation,
    }

@router.post("/folder")
def analyze_folder(request: FolderAnalysisRequest):

    explanation = analyzer.explain_folder(
        request.repository,
        request.folder_path
    )

    return {
        "repository": request.repository,
        "folder": request.folder_path,
        "analysis": explanation
    }

@router.post("/tech-stack")
def tech_stack(request: AnalysisRequest):

    result = analyzer.detect_tech_stack(
        request.repository
    )

    return {
        "repository": request.repository,
        "tech_stack": result
    }

@router.post("/architecture")
def architecture(request: AnalysisRequest):

    architecture = analyzer.architecture(
        request.repository
    )

    return {
        "repository": request.repository,
        "architecture": architecture
    }