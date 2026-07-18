from git import Repo
from git.exc import GitCommandError
from pathlib import Path
import shutil

# backend folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# backend/repos
REPO_DIR = BASE_DIR / "repos"

REPO_DIR.mkdir(exist_ok=True)


def clone_repository(repo_url: str):

    repo_name = Path(repo_url).stem

    destination = REPO_DIR / repo_name

    if destination.exists():
        shutil.rmtree(destination)

    try:
        Repo.clone_from(
            repo_url,
            destination,
            depth=1,
            single_branch=True
        )

        return {
            "success": True,
            "repository": repo_name,
            "path": str(destination)
        }

    except GitCommandError as e:

        return {
            "success": False,
            "error": str(e)
        }