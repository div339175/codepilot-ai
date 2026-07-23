from pathlib import Path
import json


class DashboardService:

    def __init__(self):
        self.repos_dir = Path("repos")
        self.indexes_dir = Path("indexes")
        self.analysis_dir = Path("analysis")

    def overview(self):

        repositories = []
        languages = set()
        frameworks = set()

        if not self.repos_dir.exists():
            return {
                "total_repositories": 0,
                "analyzed_repositories": 0,
                "total_languages": 0,
                "total_frameworks": 0,
                "repositories": []
            }

        for repo in sorted(self.repos_dir.iterdir()):

            if not repo.is_dir():
                continue

            repo_name = repo.name

            # -------- Repository Paths --------
            repo_path = self.repos_dir / repo_name
            index_dir = self.indexes_dir / repo_name
            analysis_file = self.analysis_dir / f"{repo_name}.json"

            # -------- Status --------
            indexed = (
                (index_dir / "code.index").exists()
                and
                (index_dir / "metadata.pkl").exists()
            )

            analyzed = analysis_file.exists()

            status = "Not Indexed"

            if indexed:
                status = "Indexed"

            # -------- Defaults --------
            repo_languages = []
            repo_frameworks = []
            generated_at = None
            analysis_ready = False
            data = {}

            # -------- Read Analysis --------
            if analyzed:
                try:
                    with open(analysis_file, "r") as f:
                        data = json.load(f)

                    status = data.get("status", "Ready")

                    tech_stack = data.get("tech_stack", {})

                    repo_languages = tech_stack.get("languages", [])
                    repo_frameworks = tech_stack.get("frameworks", [])

                    generated_at = data.get("generated_at")

                    analysis_ready = (
                        bool(data.get("summary"))
                        and bool(data.get("architecture"))
                    )

                    languages.update(repo_languages)
                    frameworks.update(repo_frameworks)

                except Exception as e:
                    print(f"Error reading {analysis_file}: {e}")

            # -------- Repository Stats --------
            file_count = sum(
                1 for f in repo_path.rglob("*")
                if f.is_file()
            )

            total_size = sum(
                f.stat().st_size
                for f in repo_path.rglob("*")
                if f.is_file()
            )

            repo_size = round(total_size / (1024 * 1024), 2)

            repositories.append({
                "repository": repo_name,
                "status": status,
                "indexed": indexed,
                "analyzed": analyzed,

                "generated_at": generated_at,

                "languages": repo_languages,
                "frameworks": repo_frameworks,

                "file_count": file_count,
                "repository_size": f"{repo_size} MB",

                "analysis_ready": analysis_ready,
            })

        return {
            "total_repositories": len(repositories),
            "analyzed_repositories": sum(
                repo["analyzed"] for repo in repositories
            ),
            "total_languages": len(languages),
            "total_frameworks": len(frameworks),
            "repositories": repositories,
        }