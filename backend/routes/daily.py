# routes/daily.py

from fastapi import APIRouter
from database import SessionLocal
from models.daily_content import DailyContent
from services.ai_service import generate_daily_content

router = APIRouter()

@router.get("/daily/{day}")
def get_daily_content(day: int):
    """
    - إذا كان محتوى اليوم موجود في DB → نرجعه
    - إذا غير موجود → نولّده بالـ AI ونخزنه
    """

    db = SessionLocal()

    try:
        # نبحث عن محتوى اليوم
        content = db.query(DailyContent).filter(DailyContent.day == day).first()

        if content:
            # موجود → نرجعه مباشرة
            return {
                "day": content.day,
                "message": content.message,
                "duaa": content.duaa,
                "quran": content.quran
            }

        # غير موجود → نولّده
        generated = generate_daily_content(day)

        new_content = DailyContent(
            day=day,
            message=generated["message"],
            duaa=generated["duaa"],
            quran=generated["quran"]
        )

        db.add(new_content)
        db.commit()

        return generated

    finally:
        db.close()
