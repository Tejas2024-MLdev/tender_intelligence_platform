from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.db.base_model import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False
    )

    uploaded_by: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    file_name: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    minio_object_name: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="UPLOADED"
    )