from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    employer: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    company_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("companies.id"), nullable=True)
    company: Mapped[Optional["Company"]] = relationship("Company", back_populates="contacts")
