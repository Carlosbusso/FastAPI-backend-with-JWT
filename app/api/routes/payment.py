from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.payment import PaymentWebhook
from app.services.payment_service import PaymentService
from app.core.security import verify_api_key

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/webhook")
def receive_payment(
    data: PaymentWebhook,
    db: Session = Depends(get_db),
    _: str = Depends(verify_api_key)
):

    try:
        payment = PaymentService.process_payment(db, data)
        return {"message": "Payment processed", "payment_id": payment.id}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
