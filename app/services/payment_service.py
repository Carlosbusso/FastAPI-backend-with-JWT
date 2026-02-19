from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.payment import Payment
from app.models.debt import Debt


class PaymentService:

    @staticmethod
    def process_payment(db: Session, data):

        debt = db.query(Debt).filter(Debt.id == data.debt_id).first()

        if not debt:
            raise ValueError("Debt not found")

        if debt.status == "PAID":
            raise ValueError("Debt already paid")

        payment = Payment(
            debt_id=data.debt_id,
            external_reference=data.external_reference,
            amount=data.amount,
            payment_date=data.payment_date
        )

        db.add(payment)

        try:
            debt.remaining_amount -= data.amount

            if debt.remaining_amount <= 0:
                debt.status = "PAID"
                debt.remaining_amount = 0
            else:
                debt.status = "PARTIAL"

            db.commit()

        except IntegrityError:
            db.rollback()
            raise ValueError("Payment already processed")

        db.refresh(payment)
        return payment
