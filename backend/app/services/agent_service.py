from app.core.llm import ask_llm

class AgentService:

    def ask(
        self,
        repository: str,
        current_file: str | None,
        current_content: str,
        message: str,
    ):

        prompt = f"""
You are CodePilot AI, an AI software engineer.

Repository:
{repository}

Current File:
{current_file}

Current File Content:
{current_content}

User Request:
{message}

Instructions:
- Answer only using the provided file when possible.
- Explain code clearly.
- Use Markdown.
- If the information is not present in this file, say so.
"""

        answer = ask_llm(prompt)

        return {
            "response": answer
        }