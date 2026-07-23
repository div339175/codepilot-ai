from pathlib import Path
import json


class DashboardService:

    def __init__(self):
        self.analysis_dir = Path("analysis")
        self.repo_dir = Path("repos")

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

            try:

                with open(file, "r") as f:
                    data = json.load(f)

                tech_stack = data.get("tech_stack", {})

                repo_languages = tech_stack.get("languages", [])
                repo_frameworks = tech_stack.get("frameworks", [])

                # Repository path
                repo_name = data.get("repository")
                repo_path = self.repo_dir / repo_name

                # Count files
                file_count = 0

                if repo_path.exists():
                    file_count = sum(
                        1 for f in repo_path.rglob("*")
                        if f.is_file()
                    )

                # Repository size (MB)
                total_size = 0

                if repo_path.exists():
                    total_size = sum(
                        f.stat().st_size
                        for f in repo_path.rglob("*")
                        if f.is_file()
                    )

                repo_size = round(total_size / (1024 * 1024), 2)

                repositories.append({
                    "repository": repo_name,
                    "generated_at": data.get("generated_at"),
                    "languages": repo_languages,
                    "frameworks": repo_frameworks,

                    "file_count": file_count,
                    "repository_size": f"{repo_size} MB",

                    "analysis_ready": bool(data.get("summary"))
                    and bool(data.get("architecture"))
                })

                languages.update(repo_languages)
                frameworks.update(repo_frameworks)

            except Exception as e:
                print(f"ERROR while reading {file}: {e}")

        return {
            "total_repositories": len(repositories),
            "analyzed_repositories": len(repositories),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories
        }