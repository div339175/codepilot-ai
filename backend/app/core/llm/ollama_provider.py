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
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]