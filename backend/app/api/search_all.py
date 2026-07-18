from fastapi import APIRouter

from app.schemas.search_all import SearchAllRequest
from app.services.multi_repository_service import MultiRepositoryService

router = APIRouter(
    prefix="/search",
    tags=["Multi Repository Search"]
)

service = MultiRepositoryService()


@router.post("/all")
def search_all(request: SearchAllRequest):

    results = service.search_all(
        query=request.query,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "total_results": len(results),
        "results": results
    }