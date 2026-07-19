from app.core.search import semantic_search
from app.core.llm import ask_llm


class RepositoryService:

    def ask(
        self,
        repository: str,
        question: str
    ):

        results = semantic_search(
            repository=repository,
            query=question,
            top_k=5
        )

        if not results:
            return {
                "answer": "No relevant code found.",
                "sources": []
            }

        context = ""
        sources = []

        for item in results:

            context += f"""
Repository: {item['repository']}

File: {item['file']}

Language: {item['language']}

Code:

{item['chunk']}

--------------------
"""

            sources.append({
                "file": item["file"],
                "score": item["score"]
            })

        prompt = f"""
You are an expert software engineer.

Answer ONLY using the provided repository context.

If the answer is not present in the context, reply exactly:

"I couldn't find this information inside the repository."

Repository Context:

{context}

Question:

{question}
"""

        answer = ask_llm(prompt)

        return {
            "answer": answer,
            "sources": sources
        }