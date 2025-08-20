from __future__ import annotations

import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.db import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(255))
    domain: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    contacts: Mapped[List["Contact"]] = relationship("Contact", back_populates="company")
    applications: Mapped[List["Application"]] = relationship("Application", back_populates="company")
