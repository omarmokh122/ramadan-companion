# main.py

from fastapi import FastAPI
from routes.assistant import router as assistant_router
from routes.daily import router as daily_router
from database import engine
from models.daily_content import DailyContent
from database import Base
from models.user import User
from routes.users import router as users_router




app = FastAPI(
    title="Ramadan Companion API",
    description="Backend for AI-powered Ramadan Companion",
    version="1.0.0"
)

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)


# ربط Routes
app.include_router(assistant_router)
app.include_router(daily_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "Ramadan Companion Backend is running 🌙"}
