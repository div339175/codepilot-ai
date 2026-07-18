from app.analyzers.repository_analyzer import RepositoryAnalyzer
from app.core.llm import ask_llm


class RepositoryComparator:

    def __init__(self):

        self.analyzer = RepositoryAnalyzer()

    def compare(
        self,
        repository_1: str,
        repository_2: str
    ):

        # Generate repository summaries
        summary_1 = self.analyzer.generate_summary(repository_1)
        summary_2 = self.analyzer.generate_summary(repository_2)

        # Detect tech stacks
        tech_stack_1 = self.analyzer.detect_tech_stack(repository_1)
        tech_stack_2 = self.analyzer.detect_tech_stack(repository_2)

        prompt = f"""
You are a senior software architect.

Compare the following repositories.

==================================================

Repository 1

Name:
{repository_1}

Summary:
{summary_1}

Tech Stack:
{tech_stack_1}

==================================================

Repository 2

Name:
{repository_2}

Summary:
{summary_2}

Tech Stack:
{tech_stack_2}

==================================================

Compare these repositories based on:

1. Project Purpose
2. Overall Architecture
3. Technologies Used
4. Folder Organization
5. Design Patterns
6. Strengths
7. Weaknesses
8. Scalability
9. Maintainability
10. Which project is better suited for different use cases

Finally provide an overall recommendation.

Return the answer in well-formatted Markdown.
"""

        return ask_llm(prompt)