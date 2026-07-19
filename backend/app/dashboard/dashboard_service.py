from pathlib import Path
import json


class DashboardService:

    def __init__(self):
        self.analysis_dir = Path("analysis")

    def overview(self):

        repositories = []

        languages = set()

        frameworks = set()

        if not self.analysis_dir.exists():
            return {
                "total_repositories": 0,
                "analyzed_repositories": 0,
                "total_languages": 0,
                "total_frameworks": 0,
                "repositories": []
            }

        for file in self.analysis_dir.glob("*.json"):

            with open(file, "r") as f:
                data = json.load(f)

            repositories.append({
                "repository": data["repository"],
                "generated_at": data.get("generated_at"),
                "languages": data.get("languages", []),
                "frameworks": data.get("frameworks", []),
                "summary_length": data.get("summary_length", 0),
                "architecture_length": data.get("architecture_length", 0)
            })

            languages.update(data.get("languages", []))
            frameworks.update(data.get("frameworks", []))

        return {
            "total_repositories": len(repositories),
            "analyzed_repositories": len(repositories),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories
        }