from fastapi import APIRouter, HTTPException

from app.core.repository_registry import RepositoryRegistry

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"],
)

registry = RepositoryRegistry()


@router.get("/")
def list_repositories():

    return {
        "repositories": registry.list_repositories()
    }


@router.get("/{repository}")
def repository_metadata(repository: str):

    metadata = registry.metadata(repository)

    if metadata is None:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    return metadata


@router.delete("/{repository}")
def delete_repository(repository: str):

    deleted = registry.delete(repository)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    return {
        "message": f"{repository} deleted successfully"
    }