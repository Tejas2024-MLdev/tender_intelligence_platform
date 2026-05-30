from backend.services.storage.minio_service import (
    MinioService,
)

from backend.services.rag.pdf_service import (
    PDFService,
)

from backend.services.rag.chunking_service import (
    ChunkingService,
)

from backend.services.rag.embedding_service import (
    EmbeddingService,
)

from backend.services.rag.qdrant_service import (
    QdrantService,
)


class IngestionService:

    @classmethod
    def ingest_document(
        cls,
        document,
    ):

        pdf_path = (
            MinioService.download_document(
                document.minio_object_name
            )
        )

        text = (
            PDFService.extract_text(
                pdf_path
            )
        )

        chunks = (
            ChunkingService.chunk_text(
                text
            )
        )

        vectors = (
            EmbeddingService.embed(
                chunks
            )
        )

        QdrantService.insert_chunks(
            document_id=str(
                document.id
            ),
            chunks=chunks,
            vectors=vectors,
        )

        return len(chunks)
    