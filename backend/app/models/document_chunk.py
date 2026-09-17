from sqlalchemy import ForeignKey, Text

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class DocumentChunk(Base):
    __tablename__ = 'document_chunks'

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey('documents.id'))

    chunk_index: Mapped[int]

    chunk_text: Mapped[Text] = mapped_column(
        Text
    )
