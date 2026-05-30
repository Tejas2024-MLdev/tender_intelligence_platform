from openai import OpenAI

from backend.core.config import settings

from .base import BaseLLMProvider


class OpenRouterProvider(
    BaseLLMProvider
):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(
        self,
        context: str,
        question: str,
    ):

        prompt = f"""
Context:
{context}

Question:
{question}

Instructions:
Answer only using the provided context.
If the answer is not found in the context,
say "I could not find this information in the document."
"""

        response = (
            self.client.chat.completions.create(
                model=settings.OPENROUTER_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
        )

        return (
            response
            .choices[0]
            .message.content
        )