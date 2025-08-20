from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.db import get_db
from ..models import Application
from ..schemas.application import ApplicationCreate, ApplicationRead

router = APIRouter()


@router.get("/", response_model=List[ApplicationRead])
def list_applications(db: Session = Depends(get_db)):
    return db.query(Application).order_by(Application.created_at.desc()).all()


@router.post("/", response_model=ApplicationRead)
def create_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    application = Application(
        company_id=payload.company_id,
        job_title=payload.job_title,
        status=payload.status,
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("/{application_id}", response_model=ApplicationRead)
def get_application(application_id: str, db: Session = Depends(get_db)):
    application = db.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
