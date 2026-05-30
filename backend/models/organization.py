# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column

# from backend.db.base import Base


# class Organization(Base):
#     __tablename__ = "organizations"

#     id: Mapped[int] = mapped_column(
#         primary_key=True
#     )

#     name: Mapped[str] = mapped_column(
#         String(255),
#         unique=True,
#         nullable=False
#     )


from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.db.base_model import BaseModel
from sqlalchemy.orm import relationship


class Organization(BaseModel):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )    

    users = relationship(
    "User",
    back_populates="organization"
)