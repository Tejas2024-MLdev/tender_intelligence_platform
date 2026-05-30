from io import BytesIO
from uuid import uuid4

from minio import Minio

from backend.core.config import settings


class MinioService:

    client = Minio(
        settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=False,
    )

    @classmethod
    def ensure_bucket(cls):

        if not cls.client.bucket_exists(
            settings.MINIO_BUCKET
        ):
            cls.client.make_bucket(
                settings.MINIO_BUCKET
            )

    @classmethod
    def upload_document(
        cls,
        organization_id: str,
        filename: str,
        content: bytes,
    ):

        object_name = (
            f"{organization_id}/"
            f"{uuid4()}/"
            f"{filename}"
        )

        cls.client.put_object(
            bucket_name=settings.MINIO_BUCKET,
            object_name=object_name,
            data=BytesIO(content),
            length=len(content),
        )

        return object_name