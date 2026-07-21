from pathlib import Path


class ExplorerService:

    def __init__(self):

        self.repositories_dir = Path("repos")   # change if needed

    def repository_tree(self, repository: str):

        repo = self.repositories_dir / repository

        if not repo.exists():
            raise FileNotFoundError(repository)

        return {
            "name": repository,
            "type": "folder",
            "path": "",
            "children": self._build_tree(repo, repo)
        }

    def _build_tree(self, current: Path, root: Path):

        children = []

        for item in sorted(
            current.iterdir(),
            key=lambda p: (p.is_file(), p.name.lower())
        ):

            if item.name.startswith("."):
                continue

            relative = item.relative_to(root).as_posix()

            if item.is_dir():

                children.append({
                    "name": item.name,
                    "path": relative,
                    "type": "folder",
                    "children": self._build_tree(item, root)
                })

            else:

                children.append({
                    "name": item.name,
                    "path": relative,
                    "type": "file"
                })

        return children