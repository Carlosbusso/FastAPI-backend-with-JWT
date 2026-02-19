from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.debt import DebtCreate, DebtResponse
from app.services.debt_service import DebtService

router = APIRouter(prefix="/debts", tags=["Debts"])

@router.post("/", response_model=DebtResponse)
def create_debt(data: DebtCreate, db: Session = Depends(get_db)):
    return DebtService.create_debt(db, data)
