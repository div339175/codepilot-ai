from app.core.search import semantic_search
from app.core.llm import ask_llm


class RepositoryService:

    ...

    def ask(self, question: str):

        results = semantic_search(question, top_k=5)

        context = ""

        for item in results:

            context += f"""
File: {item['file']}

Language: {item['language']}

Code:

{item['chunk']}

--------------------
"""

        prompt = f"""
You are an expert software engineer.

Answer ONLY using the provided repository context.

If the answer is not present,
say:

"I couldn't find this information inside the repository."

Repository Context:

{context}

Question:

{question}
"""

        return ask_llm(prompt)