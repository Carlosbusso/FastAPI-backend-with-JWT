from sqlalchemy.orm import Session
from app.models.customer import Customer

class CustomerService:

    @staticmethod
    def create_customer(db: Session, data):
        customer = Customer(
            document_number=data.document_number,
            full_name=data.full_name,
            email=data.email
        )

        db.add(customer)
        db.commit()
        db.refresh(customer)

        return customer
