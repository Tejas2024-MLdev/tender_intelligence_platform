from backend.services.rag.search_service import (
    SearchService,
)

from backend.services.rag.llm_service import (
    LLMService,
)


class RAGService:

    @classmethod
    def ask(
        cls,
        question: str,
    ):

        chunks = SearchService.search(
            question
        )

        context = "\n\n".join(
            item["chunk"]
            for item in chunks
        )

        answer = (
            LLMService.generate(
                context=context,
                question=question,
            )
        )

        return {
            "answer": answer,
            "sources": chunks,
        }