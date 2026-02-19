from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    debt_id = Column(Integer, ForeignKey("debts.id"), nullable=False)

    external_reference = Column(String, nullable=False, unique=True)
    amount = Column(Numeric(10, 2), nullable=False)
    source = Column(String, default="CASHEA")

    payment_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    debt = relationship("Debt", backref="payments")
