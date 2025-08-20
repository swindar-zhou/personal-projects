from pydantic import BaseModel
from typing import Optional


class CompanyBase(BaseModel):
    name: str
    domain: Optional[str] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyRead(CompanyBase):
    id: str

    class Config:
        from_attributes = True
