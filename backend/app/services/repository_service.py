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
Repository Context
==================

{context}

User Question
=============

{question}

Instructions
============

Answer only using the repository context.

Return the answer in Markdown.

Structure your response like this:

# Overview

Explain the concept in simple English.

# How It Works

Use a markdown bullet list.

Example:

- Generate embeddings
- Search FAISS
- Retrieve top chunks
- Generate final answer

# Important Files

Return as a markdown bullet list.

Example:

- backend/app/core/search.py
- backend/app/services/repository_service.py

# Key Functions

Mention important functions and what they do.

# Summary

Provide a short conclusion.

Do NOT return JSON.

Do NOT repeat the raw repository context.
"""
        
        answer = ask_llm(prompt)

        return {
            "answer": answer,
            "sources": sources
        }