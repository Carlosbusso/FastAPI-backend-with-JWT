from sqlalchemy.orm import Session
from app.models.debt import Debt
from decimal import Decimal

class DebtService:

    @staticmethod
    def create_debt(db: Session, data):
        debt = Debt(
            customer_id=data.customer_id,
            total_amount=data.total_amount,
            remaining_amount=Decimal(data.total_amount),
            status="PENDING"
        )

        db.add(debt)
        db.commit()
        db.refresh(debt)

        return debt
