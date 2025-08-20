from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.db import get_db
from ..models import Task
from ..schemas.task import TaskCreate, TaskRead

router = APIRouter()


@router.get("/", response_model=List[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@router.post("/", response_model=TaskRead)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        type=payload.type,
        due_at=None,
        related_contact_id=payload.related_contact_id,
        related_application_id=payload.related_application_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: str, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
