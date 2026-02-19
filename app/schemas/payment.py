from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class PaymentWebhook(BaseModel):
    debt_id: int
    external_reference: str
    amount: Decimal
    payment_date: datetime
