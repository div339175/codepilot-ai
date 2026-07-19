from pathlib import Path

from app.core.parser import parse_repository
from app.core.file_reader import read_file
from app.core.llm import ask_llm
from app.analyzers.tech_stack_detector import TechStackDetector
from app.analyzers.architecture_analyzer import ArchitectureAnalyzer
from app.analyzers.api_doc_analyzer import APIDocumentationAnalyzer


class RepositoryAnalyzer:

    def generate_summary(self, repository: str):

        repo_path = Path("repos") / repository

        files = parse_repository(repo_path)

        context = ""

        for file in files:

            if not file.content.strip():
                continue

            context += f"""
File: {file.path}

Language: {file.language}

Content:
{file.content[:1500]}

-----------------------------------
"""

        prompt = f"""
You are an expert software architect.

Analyze the following repository.

Provide:

1. Project purpose
2. Main features
3. Technologies used
4. High-level architecture
5. Important folders
6. Overall workflow

Repository:

{context}
"""

        return ask_llm(prompt)

    def explain_file(self, repository: str, file_path: str):

        full_path = Path("repos") / repository / file_path

        if not full_path.exists():
            return "File not found."

        content = read_file(full_path)

        if not content.strip():
            return "File is empty or could not be read."

        prompt = f"""
You are an expert software engineer.

Analyze the following source code.

Provide:

1. Purpose
2. Main functions
3. Classes
4. Important algorithms
5. Dependencies
6. Time complexity (if applicable)
7. How this file fits into the overall project

Source Code:

{content}
"""

        return ask_llm(prompt)
    

    def explain_folder(self, repository: str, folder_path: str):

        folder = Path("repos") / repository / folder_path

        if not folder.exists():
            return "Folder not found."

        context = ""

        for file in folder.rglob("*"):

            if not file.is_file():
                continue

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            except Exception:
                continue

            context += f"""
File: {file.relative_to(folder)}

{content[:1000]}

-------------------------
"""

        prompt = f"""
You are an expert software architect.

Analyze this folder.

Explain:

1. Folder responsibility
2. Major files
3. How the files interact
4. Important classes/functions
5. How this folder fits into the repository

Folder Content:

{context}
"""

        return ask_llm(prompt)
    
    
    def detect_tech_stack(self, repository: str):

        detector = TechStackDetector()

        return detector.detect(repository)
    
    def analyze_architecture(self, repository: str):

        analyzer = ArchitectureAnalyzer()

        return analyzer.generate(repository)
    
    def api_documentation(self, repository: str):

        analyzer = APIDocumentationAnalyzer()

        return analyzer.generate(repository)