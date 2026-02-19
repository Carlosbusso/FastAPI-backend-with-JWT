from fastapi import FastAPI
from app.core.database import engine, Base
import app.models  # 👈 Importa el paquete completo
from app.api.routes import payment
from app.api.routes import customer
from app.api.routes import debt

app = FastAPI(title="Task Manager API")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "running"}

app.include_router(payment.router, prefix="/api/v1")
app.include_router(customer.router, prefix="/api/v1")
app.include_router(debt.router, prefix="/api/v1")
