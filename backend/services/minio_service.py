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



