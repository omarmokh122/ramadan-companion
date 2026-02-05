# routes/users.py

from fastapi import APIRouter
from database import SessionLocal
from models.user import User

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(payload: dict):
    """
    إنشاء مستخدم جديد
    """

    db = SessionLocal()

    try:
        user = User(
            name=payload.get("name"),
            email=payload.get("email"),
            goal=payload.get("goal", "عبادة")
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "goal": user.goal
        }

    finally:
        db.close()


@router.get("/{user_id}")
def get_user(user_id: int):
    """
    جلب بيانات مستخدم
    """

    db = SessionLocal()

    try:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return {"error": "User not found"}

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "goal": user.goal
        }

    finally:
        db.close()
