from pathlib import Path
import json
import re

from app.core.llm import ask_llm
from app.core.parser import read_repository_code


class ReviewService:

    def __init__(self):
        self.review_dir = Path("reviews")
        self.review_dir.mkdir(exist_ok=True)

    def review(self, repository: str):

        review_file = self.review_dir / f"{repository}.json"

        # Return cached review if available
        if review_file.exists():
            with open(review_file, "r") as f:
                return json.load(f)

        # Repository path
        repo_path = Path("repos") / repository

        print("Repository:", repository)
        print("Current Working Directory:", Path.cwd())
        print("Looking for:", repo_path.resolve())
        print("Exists:", repo_path.exists())

        if not repo_path.exists():
            raise FileNotFoundError(f"Repository '{repository}' not found.")

        # Read all supported source files
        code = read_repository_code(repo_path)

        if not code.strip():
            raise ValueError(
                f"No supported source files found in '{repository}'."
            )

        # Limit context for local models
        code = code[:8000]

        prompt = f"""
You are an expert software engineer.

Review the following repository.

Analyze the code and identify:

1. Bugs
2. Security issues
3. Code smells
4. Performance improvements
5. Best practices

Give each point as a short sentence.

Finally assign an overall score out of 10.

Return ONLY valid JSON.

Example:

{{
    "bugs":[
        "Bug 1"
    ],
    "security_issues":[
        "Issue 1"
    ],
    "code_smells":[
        "Smell 1"
    ],
    "performance_suggestions":[
        "Suggestion 1"
    ],
    "best_practices":[
        "Practice 1"
    ],
    "overall_score":8.4
}}

Repository Code:

{code}
"""

        response = ask_llm(prompt)

        # Remove markdown if model returns ```json
        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

        try:
            response = response.strip()

            # Remove markdown fences
            response = re.sub(r"^```json", "", response, flags=re.MULTILINE)
            response = re.sub(r"^```", "", response, flags=re.MULTILINE)
            response = response.strip()

            # Extract first JSON object if extra text exists
            match = re.search(r"\{.*\}", response, re.DOTALL)

            if match:
                response = match.group(0)

            review = json.loads(response)

        except Exception:

            review = {
                "bugs": [],
                "security_issues": [],
                "code_smells": [],
                "performance_suggestions": [],
                "best_practices": [],
                "overall_score": 0,
                "raw_response": response
            }

        review["repository"] = repository

        with open(review_file, "w") as f:
            json.dump(review, f, indent=4)

        return review