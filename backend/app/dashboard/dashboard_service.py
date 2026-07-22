from pathlib import Path
import json


class DashboardService:

    def __init__(self):
        self.analysis_dir = Path("analysis")

    def overview(self):

        print("Dashboard endpoint called")

        print("Analysis directory:", self.analysis_dir.resolve())
        print("Exists:", self.analysis_dir.exists())
        print("Files:", list(self.analysis_dir.glob("*.json")))

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

            # ✅ Read tech_stack
            tech_stack = data.get("tech_stack", {})

            repo_languages = tech_stack.get("languages", [])
            repo_frameworks = tech_stack.get("frameworks", [])

            repositories.append({
                "repository": data["repository"],
                "generated_at": data.get("generated_at"),

                "languages": repo_languages,
                "frameworks": repo_frameworks,

                # Better values than 0
                "summary_length": len(data.get("summary", "")),
                "architecture_length": len(data.get("architecture", ""))
            })

            languages.update(repo_languages)
            frameworks.update(repo_frameworks)
            print("Returning:", {
                "total_repositories": len(repositories),
                "repositories": repositories
            })

        return {
            "total_repositories": len(repositories),
            "analyzed_repositories": len(repositories),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories
        }