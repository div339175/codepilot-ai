from datetime import datetime

from app.analyzers.repository_analyzer import RepositoryAnalyzer
from app.core.analysis_cache import AnalysisCache


class AnalysisService:

    def __init__(self):

        self.analyzer = RepositoryAnalyzer()
        self.cache = AnalysisCache()

    def generate(self, repository: str):

        # Dashboard will show "Analyzing"
        self.cache.save(
            repository,
            {
                "repository": repository,
                "status": "Analyzing",
                "summary": None,
                "architecture": None,
                "tech_stack": {},
                "generated_at": None,
            }
        )

        summary = self.analyzer.generate_summary(repository)

        tech_stack = self.analyzer.detect_tech_stack(repository)

        architecture = self.analyzer.analyze_architecture(repository)

        data = {
            "repository": repository,
            "status": "Ready",
            "summary": summary,
            "tech_stack": tech_stack,
            "architecture": architecture,
            "generated_at": datetime.now().isoformat(),
        }

        self.cache.save(repository, data)

        return data