from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.rag.ingestion_service import (
    IngestionService,
)

from backend.core.dependencies import get_current_user
from backend.db.session import get_db
from backend.services.document_service import (
    DocumentService,
)

from backend.schemas.document import (
    DocumentUploadResponse,
    DocumentResponse,
)


from backend.services.storage.minio_service import (
    MinioService,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



@router.post(
    "/upload",
    response_model=DocumentUploadResponse
)
async def upload_document(
    file: UploadFile = File(...),
    current_user: dict = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(get_db),
):

    content = await file.read()

    object_name = (
        MinioService.upload_document(
            organization_id=current_user[
                "organization_id"
            ],
            filename=file.filename,
            content=content,
        )
    )

    document = (
        await DocumentService.create_document(
            db=db,
            organization_id=current_user[
                "organization_id"
            ],
            user_id=current_user["sub"],
            file_name=file.filename,
            object_name=object_name,
        )
    )

    return DocumentUploadResponse(
        document_id=str(document.id),
        file_name=document.file_name,
        status=document.status,
    )



@router.get(
    "",
    response_model=List[
        DocumentResponse
    ]
)
async def list_documents(
    current_user: dict = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(get_db),
):

    return await (
        DocumentService.list_documents(
            db=db,
            organization_id=current_user[
                "organization_id"
            ]
        )
    )    


@router.post("/{document_id}/ingest")
async def ingest_document(
    document_id: str,
    current_user: dict = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(get_db),
):

    document = (
        await DocumentService.get_document(
            db=db,
            document_id=document_id,
            organization_id=current_user[
                "organization_id"
            ],
        )
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    chunk_count = (
        IngestionService.ingest_document(
            document
        )
    )

    return {
        "document_id": str(document.id),
        "chunks_created": chunk_count,
    }