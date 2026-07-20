import os
import ollama

from .base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self):

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "qwen2.5:7b"
        )

    def ask(self, prompt: str):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
                You are CodePilot AI, an expert software engineer.

                Rules:

                - Explain code in clear, professional English.
                - Answer in Markdown.
                - Never return JSON unless the user explicitly asks for JSON.
                - Use headings and bullet points.
                - Use short code snippets only when helpful.
                - Do not copy the repository context verbatim.
                - Summarize and explain instead of listing raw data.
                """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        return response["message"]["content"].strip()