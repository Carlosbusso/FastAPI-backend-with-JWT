from pydantic import BaseModel, EmailStr

class CustomerCreate(BaseModel):
    document_number: str
    full_name: str
    email: EmailStr | None = None


class CustomerResponse(BaseModel):
    id: int
    document_number: str
    full_name: str
    email: str | None
    is_active: bool

    class Config:
        from_attributes = True
