from pathlib import Path
import shutil


class RepositoryRegistry:

    def __init__(self):
        self.repo_dir = Path("repos")

    def list_repositories(self):
        """
        Return all cloned repositories.
        """

        if not self.repo_dir.exists():
            return []

        repositories = []

        for repo in self.repo_dir.iterdir():

            if repo.is_dir():
                repositories.append(repo.name)

        return sorted(repositories)

    def exists(self, repository: str):
        """
        Check whether a repository exists.
        """

        return (self.repo_dir / repository).exists()

    def delete(self, repository: str):
        """
        Delete a repository.
        """

        repo_path = self.repo_dir / repository

        if not repo_path.exists():
            return False

        shutil.rmtree(repo_path)

        return True

    def metadata(self, repository: str):
        """
        Return repository metadata.
        """

        repo_path = self.repo_dir / repository

        if not repo_path.exists():
            return None

        total_files = sum(
            1
            for file in repo_path.rglob("*")
            if file.is_file()
        )

        return {
            "name": repository,
            "path": str(repo_path),
            "total_files": total_files,
        }