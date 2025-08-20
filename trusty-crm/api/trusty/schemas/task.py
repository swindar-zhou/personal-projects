from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    type: str
    due_at: Optional[str] = None
    related_contact_id: Optional[str] = None
    related_application_id: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: str

    class Config:
        from_attributes = True
