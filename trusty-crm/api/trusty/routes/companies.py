from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.db import get_db
from ..models import Company
from ..schemas.company import CompanyCreate, CompanyRead

router = APIRouter()


@router.get("/", response_model=List[CompanyRead])
def list_companies(db: Session = Depends(get_db)):
    return db.query(Company).order_by(Company.name).all()


@router.post("/", response_model=CompanyRead)
def create_company(payload: CompanyCreate, db: Session = Depends(get_db)):
    company = Company(name=payload.name, domain=payload.domain)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: str, db: Session = Depends(get_db)):
    company = db.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
