from pathlib import Path

from app.core.parser import parse_repository
from app.core.llm import ask_llm


class ArchitectureAnalyzer:

    def generate(self, repository: str):

        repo_path = Path("repos") / repository

        files = parse_repository(repo_path)

        context = ""

        for file in files:

            context += f"""
File: {file.path}

Language: {file.language}

{file.content[:800]}

--------------------
"""

        prompt = f"""
You are an expert software architect.

Analyze this repository.

Generate:

1. Overall architecture
2. Major components
3. Data flow
4. Layer responsibilities
5. Entry points
6. External services
7. Mermaid flowchart

Repository:

{context}
"""

        return ask_llm(prompt)