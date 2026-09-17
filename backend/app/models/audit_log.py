from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    action: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    resource_type: Mapped[str] = mapped_column(
        String(100),
    )

    resource_id: Mapped[str] = mapped_column(
        String(255),
    )

    details: Mapped[str] = mapped_column(
        Text
    )

    ip_address: Mapped[str] = mapped_column(
        String(100),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )
