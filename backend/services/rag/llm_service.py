from backend.services.llm.factory import (
    LLMFactory,
)


class LLMService:

    @staticmethod
    def generate(
        context: str,
        question: str,
    ):

        provider = (
            LLMFactory.get_provider()
        )

        return provider.generate(
            context=context,
            question=question,
        )