from fastapi import APIRouter

from app.schemas.search import SearchRequest
from app.core.search import semantic_search

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search(request: SearchRequest):

    results = semantic_search(
        repository=request.repository,
        query=request.query,
        top_k=request.top_k
    )

    return {
        "repository": request.repository,
        "query": request.query,
        "results": results
    }