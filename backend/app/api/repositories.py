from fastapi import APIRouter, HTTPException
from fastapi import Query
from app.core.repository_registry import RepositoryRegistry
from app.services.explorer_service import ExplorerService
from app.services.file_service import FileService
from pathlib import Path
from app.core.tree_builder import build_tree


explorer = ExplorerService()
file_service = FileService()

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

@router.get("/{repository}/tree")
def repository_tree(repository: str):

    try:

        return explorer.repository_tree(repository)

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

@router.get("/{repository}/file")
def repository_file(
        repository: str,
        path: str = Query(...)
    ):

        try:

            return file_service.read_file(
                repository,
                path
            )

        except FileNotFoundError:

            raise HTTPException(
                status_code=404,
                detail="File not found"
            )

        except IsADirectoryError:

            raise HTTPException(
                status_code=400,
                detail="Cannot open folder"
            )
        
@router.get("/repository-tree")
def repository_tree(repo_path: str):
    path = Path(repo_path)
    return build_tree(path, path)