from pydantic import BaseModel
from decimal import Decimal

class DebtCreate(BaseModel):
    customer_id: int
    total_amount: Decimal


class DebtResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: Decimal
    remaining_amount: Decimal
    status: str

    class Config:
        from_attributes = True
