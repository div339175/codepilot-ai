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

        indexes_dir = Path("indexes")

        for repo in self.repo_dir.iterdir():

            if repo.is_dir():

                indexed = (
                    (indexes_dir / repo.name / "code.index").exists()
                    and
                    (indexes_dir / repo.name / "metadata.pkl").exists()
                )

                repositories.append(
                    {
                        "name": repo.name,
                        "indexed": indexed,
                    }
                )

        return sorted(repositories, key=lambda r: r["name"])

    def exists(self, repository: str):
        """
        Check whether a repository exists.
        """

        return (self.repo_dir / repository).exists()

    def delete(self, repository: str):
        
        # Delete repository
        repo_path = self.repo_dir / repository
        if repo_path.exists():
            shutil.rmtree(repo_path)

        # Delete FAISS index
        index_path = Path("indexes") / repository
        if index_path.exists():
            shutil.rmtree(index_path)

        # Delete analysis cache
        analysis_file = Path("analysis") / f"{repository}.json"
        if analysis_file.exists():
            analysis_file.unlink()

        # Delete review cache
        review_file = Path("reviews") / f"{repository}.json"
        if review_file.exists():
            review_file.unlink()

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