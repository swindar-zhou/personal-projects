from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    type: Mapped[str] = mapped_column(String(32))
    due_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    related_contact_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("contacts.id"), nullable=True)
    related_application_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("applications.id"), nullable=True)
