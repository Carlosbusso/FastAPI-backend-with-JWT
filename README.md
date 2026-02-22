# FastAPI Task Manager API

Backend REST API built with FastAPI for managing users, debts and payments.
Includes JWT authentication, PostgreSQL integration and clean architecture.

---

## 🚀 Technologies

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic v2
- JWT Authentication
- Alembic (migrations)

---

## 📂 Project Structure

app/
 ├── core/
 ├── models/
 ├── schemas/
 ├── routers/
 └── main.py

---

## ⚙️ Installation

1. Clone the repository

git clone https://github.com/Carlosbusso/fastapi-task-manager.git
cd fastapi-task-manager

2. Create virtual environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

Copy `.env.example` to `.env` and configure database credentials.

5. Run the server

uvicorn app.main:app --reload

---

## 🔐 Authentication

The API uses JWT authentication.

1. Login at `/login`
2. Copy the access token
3. Click "Authorize" in Swagger `/docs`
4. Paste: Bearer YOUR_TOKEN

---

## 📖 API Documentation

Swagger UI:
http://localhost:8000/docs

---

## 👨‍💻 Author

Carlos Alberto Evangelista Busso
