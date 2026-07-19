from app.analyzers.repository_analyzer import RepositoryAnalyzer
from app.core.llm import ask_llm
from app.core.analysis_cache import AnalysisCache


class RepositoryComparator:

    def __init__(self):

        self.analyzer = RepositoryAnalyzer()
        self.cache = AnalysisCache()

    def compare(self, repository_1: str, repository_2: str):

        repo1 = self.cache.load(repository_1)
        repo2 = self.cache.load(repository_2)

        # Repository 1
        if repo1 is None:

            print(f"Cache MISS: {repository_1}")

            summary_1 = self.analyzer.generate_summary(repository_1)
            tech_stack_1 = self.analyzer.detect_tech_stack(repository_1)

            self.cache.save(repository_1, {
                "repository": repository_1,
                "summary": summary_1,
                "tech_stack": tech_stack_1
            })

        else:

            print(f"Cache HIT: {repository_1}")

            summary_1 = repo1["summary"]
            tech_stack_1 = repo1["tech_stack"]

        # Repository 2
        if repo2 is None:

            print(f"Cache MISS: {repository_2}")

            summary_2 = self.analyzer.generate_summary(repository_2)
            tech_stack_2 = self.analyzer.detect_tech_stack(repository_2)

            self.cache.save(repository_2, {
                "repository": repository_2,
                "summary": summary_2,
                "tech_stack": tech_stack_2
            })

        else:

            print(f"Cache HIT: {repository_2}")

            summary_2 = repo2["summary"]
            tech_stack_2 = repo2["tech_stack"]

        prompt = f"""
    You are a senior software architect.

    Repository 1

    Name:
    {repository_1}

    Summary:
    {summary_1}

    Tech Stack:
    {tech_stack_1}

    --------------------------------------------

    Repository 2

    Name:
    {repository_2}

    Summary:
    {summary_2}

    Tech Stack:
    {tech_stack_2}

    --------------------------------------------

    Compare these repositories based on:

    1. Purpose
    2. Architecture
    3. Technologies
    4. Folder Organization
    5. Design Patterns
    6. Strengths
    7. Weaknesses
    8. Scalability
    9. Maintainability
    10. Overall Recommendation

    Return the answer in Markdown.
    """

        return ask_llm(prompt)