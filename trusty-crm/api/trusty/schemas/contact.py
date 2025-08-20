from pydantic import BaseModel
from typing import Optional


class ContactBase(BaseModel):
    full_name: str
    email: Optional[str] = None
    employer: Optional[str] = None
    company_id: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactRead(ContactBase):
    id: str

    class Config:
        from_attributes = True
