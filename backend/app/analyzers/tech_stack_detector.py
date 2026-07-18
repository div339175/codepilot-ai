from pathlib import Path


class TechStackDetector:

    LANGUAGE_MAP = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".cpp": "C++",
        ".c": "C",
        ".java": "Java",
        ".go": "Go",
        ".rs": "Rust",
        ".html": "HTML",
        ".css": "CSS",
    }

    def detect(self, repository: str):

        repo_path = Path("repos") / repository

        languages = set()
        frameworks = set()
        databases = set()
        package_managers = set()
        deployment = set()

        # Detect programming languages
        for file in repo_path.rglob("*"):

            if file.is_file() and file.suffix in self.LANGUAGE_MAP:
                languages.add(self.LANGUAGE_MAP[file.suffix])

        # Detect Python packages
        requirements = repo_path / "requirements.txt"

        if requirements.exists():

            package_managers.add("pip")

            content = requirements.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "fastapi" in content:
                frameworks.add("FastAPI")

            if "django" in content:
                frameworks.add("Django")

            if "flask" in content:
                frameworks.add("Flask")

            if "streamlit" in content:
                frameworks.add("Streamlit")

            if "sqlalchemy" in content:
                databases.add("SQLAlchemy")

            if "psycopg" in content:
                databases.add("PostgreSQL")

            if "mysql" in content:
                databases.add("MySQL")

            if "sqlite" in content:
                databases.add("SQLite")

            if "redis" in content:
                databases.add("Redis")

            if "mongodb" in content:
                databases.add("MongoDB")

        # Detect Node.js projects
        package_json = repo_path / "package.json"

        if package_json.exists():

            package_managers.add("npm")

            content = package_json.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "react" in content:
                frameworks.add("React")

            if "next" in content:
                frameworks.add("Next.js")

            if "vue" in content:
                frameworks.add("Vue")

            if "angular" in content:
                frameworks.add("Angular")

            if "express" in content:
                frameworks.add("Express")

        # Detect deployment tools
        if (repo_path / "Dockerfile").exists():
            deployment.add("Docker")

        if (repo_path / "docker-compose.yml").exists():
            deployment.add("Docker Compose")

        if (repo_path / ".github" / "workflows").exists():
            deployment.add("GitHub Actions")

        if (repo_path / "vercel.json").exists():
            deployment.add("Vercel")

        return {
            "languages": sorted(languages),
            "frameworks": sorted(frameworks),
            "databases": sorted(databases),
            "package_managers": sorted(package_managers),
            "deployment": sorted(deployment),
        }