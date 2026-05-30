# from qdrant_client import (
#     QdrantClient,
# )
# from qdrant_client.models import (
#     Distance,
#     VectorParams,
# )

# client = QdrantClient(
#     host="localhost",
#     port=6333,
# )


# class QdrantService:

#     COLLECTION = "document_chunks"

#     @classmethod
#     def create_collection(cls):

#         collections = (
#             client.get_collections()
#         )

#         names = [
#             c.name
#             for c in collections.collections
#         ]

#         if cls.COLLECTION not in names:

#             client.create_collection(
#                 collection_name=cls.COLLECTION,
#                 vectors_config=VectorParams(
#                     size=384,
#                     distance=Distance.COSINE,
#                 ),
#             )



from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

client = QdrantClient(
    host="localhost",
    port=6333,
)


class QdrantService:

    COLLECTION = "document_chunks"

    @classmethod
    def create_collection(cls):

        collections = (
            client.get_collections()
        )

        names = [
            c.name
            for c in collections.collections
        ]

        if cls.COLLECTION not in names:

            client.create_collection(
                collection_name=cls.COLLECTION,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

    @classmethod
    def insert_chunks(
        cls,
        document_id: str,
        chunks: list[str],
        vectors: list[list[float]],
    ):

        points = []

        for chunk, vector in zip(
            chunks,
            vectors,
        ):

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=vector,
                    payload={
                        "document_id": document_id,
                        "chunk_text": chunk,
                    },
                )
            )

        client.upsert(
            collection_name=cls.COLLECTION,
            points=points,
        )


    @classmethod
    def search(
        cls,
        query_vector,
        limit=5,
    ):

        results = client.query_points(
            collection_name=cls.COLLECTION,
            query=query_vector,
            limit=limit,
        )

        return results.points