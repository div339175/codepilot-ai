from pathlib import Path
import json
import os


class DashboardService:

    def __init__(self):
        self.analysis_dir = Path("analysis")

    def overview(self):

        print("=" * 60)
        print("Dashboard endpoint called")
        print("Current Working Directory:", os.getcwd())
        print("Analysis Directory:", self.analysis_dir.resolve())
        print("Analysis Exists:", self.analysis_dir.exists())
        print("Files Found:", list(self.analysis_dir.glob("*.json")))
        print("=" * 60)

        repositories = []
        languages = set()
        frameworks = set()

        if not self.analysis_dir.exists():
            print("Analysis directory does not exist!")

            return {
                "total_repositories": 0,
                "analyzed_repositories": 0,
                "total_languages": 0,
                "total_frameworks": 0,
                "repositories": []
            }

        for file in self.analysis_dir.glob("*.json"):

            print(f"\nReading file: {file}")

            try:

                with open(file, "r") as f:
                    data = json.load(f)

                print("Repository:", data.get("repository"))
                print("Keys:", list(data.keys()))

                tech_stack = data.get("tech_stack", {})

                repo_languages = tech_stack.get("languages", [])
                repo_frameworks = tech_stack.get("frameworks", [])

                repositories.append({
                    "repository": data.get("repository"),
                    "generated_at": data.get("generated_at"),
                    "languages": repo_languages,
                    "frameworks": repo_frameworks,
                    "summary_length": len(data.get("summary", "")),
                    "architecture_length": len(data.get("architecture", ""))
                })

                languages.update(repo_languages)
                frameworks.update(repo_frameworks)

            except Exception as e:
                print(f"ERROR while reading {file}: {e}")

        print("\nRepositories List:")
        print(repositories)

        print("\nReturning Dashboard:")
        print({
            "total_repositories": len(repositories),
            "analyzed_repositories": len(repositories),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories
        })

        return {
            "total_repositories": len(repositories),
            "analyzed_repositories": len(repositories),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories
        }