from pathlib import Path


class FileService:

    def __init__(self):
        self.repositories_dir = Path("repos")

    def read_file(self, repository: str, path: str):

        file_path = self.repositories_dir / repository / path

        if not file_path.exists():
            raise FileNotFoundError(path)

        if file_path.is_dir():
            raise IsADirectoryError(path)

        return {
            "path": path,
            "content": file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        }