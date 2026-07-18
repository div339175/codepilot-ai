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
        request.query,
        request.top_k
    )

    return {
        "query": request.query,
        "results": results
    }