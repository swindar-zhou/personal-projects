from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.db import get_db
from ..models import Contact
from ..schemas.contact import ContactCreate, ContactRead

router = APIRouter()


@router.get("/", response_model=List[ContactRead])
def list_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).order_by(Contact.full_name).all()


@router.post("/", response_model=ContactRead)
def create_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    contact = Contact(
        full_name=payload.full_name,
        email=payload.email,
        employer=payload.employer,
        company_id=payload.company_id,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.get("/{contact_id}", response_model=ContactRead)
def get_contact(contact_id: str, db: Session = Depends(get_db)):
    contact = db.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
