from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Document(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True)

    filename: Mapped[str] = mapped_column(
        String(500)
    )

    file_type: Mapped[str] = mapped_column(
        String(20)
    )

    storage_path: Mapped[str] = mapped_column(
        String(1000)
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC)

    )
