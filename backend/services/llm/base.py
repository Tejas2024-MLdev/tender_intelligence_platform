from abc import ABC
from abc import abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        context: str,
        question: str,
    ) -> str:
        pass