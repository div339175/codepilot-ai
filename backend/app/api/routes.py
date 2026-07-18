from fastapi import APIRouter
from app.schemas.repository import RepositoryRequest
from app.core.git_clone import clone_repository

router = APIRouter()

@router.post("/clone")
def clone_repo(request: RepositoryRequest):

    result = clone_repository(request.repo_url)

    return result