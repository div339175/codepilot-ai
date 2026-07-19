import os
from dotenv import load_dotenv

load_dotenv()


class LLMFactory:

    @staticmethod
    def get_provider():

        provider = os.getenv("LLM_PROVIDER", "gemini").lower()

        if provider == "gemini":
            from .gemini_provider import GeminiProvider
            return GeminiProvider()

        elif provider == "ollama":
            from .ollama_provider import OllamaProvider
            return OllamaProvider()

        raise ValueError(f"Unknown provider: {provider}")