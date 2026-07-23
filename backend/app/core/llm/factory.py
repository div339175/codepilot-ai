import os
from dotenv import load_dotenv
from app.core.llm.groq_provider import GroqProvider

load_dotenv()


class LLMFactory:

    @staticmethod
    def get_provider():

        provider = os.getenv("LLM_PROVIDER", "groq").lower()

        if provider == "gemini":
            from .gemini_provider import GeminiProvider
            return GeminiProvider()

        elif provider == "ollama":
            from .ollama_provider import OllamaProvider
            return OllamaProvider()
        elif provider == "groq":
            return GroqProvider()

        raise ValueError(f"Unknown provider: {provider}")