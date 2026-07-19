from .factory import LLMFactory

provider = LLMFactory.get_provider()


def ask_llm(prompt: str):

    return provider.ask(prompt)