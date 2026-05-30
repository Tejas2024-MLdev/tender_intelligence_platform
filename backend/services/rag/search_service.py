from backend.services.rag.embedding_service import (
    EmbeddingService,
)

from backend.services.rag.qdrant_service import (
    QdrantService,
)


class SearchService:

    @classmethod
    def search(
        cls,
        query: str,
    ):

        vector = (
            EmbeddingService.embed(
                [query]
            )[0]
        )

        results = (
            QdrantService.search(
                vector
            )
        )

        return [
            {
                "score": hit.score,
                "chunk": hit.payload[
                    "chunk_text"
                ],
            }
            for hit in results
        ]