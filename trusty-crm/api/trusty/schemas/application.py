from pydantic import BaseModel
from typing import Optional


class ApplicationBase(BaseModel):
    company_id: str
    job_title: Optional[str] = None
    status: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationRead(ApplicationBase):
    id: str

    class Config:
        from_attributes = True
