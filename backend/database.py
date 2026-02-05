# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# إنشاء قاعدة بيانات SQLite
DATABASE_URL = "sqlite:///./ramadan.db"

# Engine هو الاتصال الأساسي مع DB
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # مطلوب لـ SQLite مع FastAPI
)

# Session للتعامل مع DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base نستخدمه لتعريف الجداول
Base = declarative_base()
