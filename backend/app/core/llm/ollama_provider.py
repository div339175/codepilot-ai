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
                    "content": (
                        "You are an expert software engineer. "
                        "Always follow the user's instructions exactly. "
                        "If the user asks for JSON, return ONLY valid JSON."
                    )
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