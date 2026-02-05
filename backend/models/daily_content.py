# models/daily_content.py

from sqlalchemy import Column, Integer, Text
from database import Base

class DailyContent(Base):
    """
    هذا الجدول يخزّن محتوى كل يوم من رمضان
    """

    __tablename__ = "daily_content"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, unique=True, index=True)
    message = Column(Text)
    duaa = Column(Text)
    quran = Column(Text)
