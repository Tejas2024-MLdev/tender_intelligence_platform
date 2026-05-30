from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: UUID
    file_name: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class DocumentUploadResponse(BaseModel):
    document_id: str
    file_name: str
    status: str