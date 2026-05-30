from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.models.document import Document


class DocumentService:

    @staticmethod
    async def create_document(
        db: AsyncSession,
        organization_id: str,
        user_id: str,
        file_name: str,
        object_name: str,
    ):

        document = Document(
            organization_id=organization_id,
            uploaded_by=user_id,
            file_name=file_name,
            minio_object_name=object_name,
            status="UPLOADED",
        )

        db.add(document)

        await db.commit()

        await db.refresh(document)

        return document
    

    @staticmethod
    async def list_documents(
        db: AsyncSession,
        organization_id: str,
    ):

        result = await db.execute(
            select(Document)
            .where(
                Document.organization_id
                == organization_id
            )
            .order_by(
                Document.created_at.desc()
            )
        )

        return result.scalars().all()       