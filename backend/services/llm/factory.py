from backend.core.config import settings

from backend.services.llm.openrouter_provider import (
    OpenRouterProvider,
)


class LLMFactory:

    @staticmethod
    def get_provider():

        if (
            settings.LLM_PROVIDER
            == "openrouter"
        ):
            return OpenRouterProvider()

        raise ValueError(
            "Unsupported provider"
        )