from pathlib import Path

from app.core.parser import parse_repository
from app.core.llm import ask_llm


class APIDocumentationAnalyzer:

    def generate(self, repository: str):

        repo_path = Path("repos") / repository

        if not repo_path.exists():
            return f"Repository '{repository}' not found."

        files = parse_repository(repo_path)

        print("=" * 80)
        print("Parsed Files")
        print("=" * 80)

        context = ""

        for file in files:

            print(file.path)

            content = file.content.lower()

            # Detect FastAPI / Flask / Express API files
            if (
                "@router." in content
                or "@app." in content
                or "apirouter" in content
                or "@app.route" in content
                or "router.get(" in content
                or "router.post(" in content
                or "router.put(" in content
                or "router.delete(" in content
                or "app.get(" in content
                or "app.post(" in content
                or "app.put(" in content
                or "app.delete(" in content
            ):

                print(f"API File Found -> {file.path}")

                context += f"""
File: {file.path}

{file.content}

----------------------------------------------------------
"""

        print("=" * 80)
        print("Context Length:", len(context))
        print("=" * 80)

        if not context.strip():
            return "No API endpoints were found in this repository."

        prompt = f"""
You are a senior backend engineer.

Below are source files containing API endpoints.

Generate API documentation.

For EVERY endpoint include:

- HTTP Method
- Route
- Purpose
- Request Body
- Response
- Status Codes

Do NOT invent endpoints.

If any information is missing, write "Not specified".

Return the result in Markdown.

API Source Code:

{context}
"""

        return ask_llm(prompt)