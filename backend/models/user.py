# models/user.py

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """
    جدول المستخدمين
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    goal = Column(String, default="عبادة")
