import json
from pathlib import Path


class AnalysisCache:

    def __init__(self):

        self.analysis_dir = Path("analysis")
        self.analysis_dir.mkdir(exist_ok=True)

    def save(self, repository: str, data: dict):

        file = self.analysis_dir / f"{repository}.json"

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self, repository: str):

        file = self.analysis_dir / f"{repository}.json"

        if not file.exists():
            return None

        with open(file, encoding="utf-8") as f:
            return json.load(f)

    def exists(self, repository: str):

        return (self.analysis_dir / f"{repository}.json").exists()

    def delete(self, repository: str):

        file = self.analysis_dir / f"{repository}.json"

        if file.exists():
            file.unlink()

    def update_status(self, repository: str, status: str):

        data = self.load(repository) or {}

        data["status"] = status

        self.save(repository, data)
    