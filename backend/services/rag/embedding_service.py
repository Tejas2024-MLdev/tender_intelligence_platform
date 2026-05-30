from sentence_transformers import (
    SentenceTransformer,
)


class EmbeddingService:

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    @classmethod
    def embed(
        cls,
        texts: list[str],
    ):

        return cls.model.encode(
            texts,
            normalize_embeddings=True,
        ).tolist()