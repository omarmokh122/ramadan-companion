from fastapi import APIRouter
from database import SessionLocal
from models.user import User
from services.ai_service import ask_ai

router = APIRouter()

@router.post("/assistant")
def assistant_chat(payload: dict):
    """
    Assistant مرتبط بالمستخدم
    """

    db = SessionLocal()

    try:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        day = payload.get("day", 1)

        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return {"error": "User not found"}

        ai_response = ask_ai(
            day=day,
            goal=user.goal,  # 👈 الهدف من DB
            message=message
        )

        return {"response": ai_response}

    finally:
        db.close()
