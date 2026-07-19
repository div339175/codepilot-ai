from fastapi import APIRouter

from app.review.review_service import ReviewService
from app.schemas.review import ReviewRequest

router = APIRouter(
    prefix="/review",
    tags=["AI Review"]
)

service = ReviewService()


@router.post("/")

def review(request: ReviewRequest):

    return service.review(request.repository)