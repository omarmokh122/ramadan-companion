# services/ai_service.py

import os
from openai import OpenAI
from dotenv import load_dotenv  # ⬅️ جديد
from ai.prompts import (
    assistant_prompt,
    daily_message_prompt,
    daily_duaa_prompt,
    daily_quran_prompt
)

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# إنشاء Client للـ OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(day: int, goal: str, message: str) -> str:
    """
    هذه الدالة:
    - تبني الـ prompt
    - ترسل الطلب للـ AI
    - ترجع الرد النهائي كنص
    """

    prompt = assistant_prompt(
        day=day,
        goal=goal,
        user_message=message
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content.strip()
def generate_daily_content(day: int) -> dict:
    """
    توليد محتوى اليوم (رسالة - دعاء - ورد)
    """

    message = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": daily_message_prompt(day)}],
        temperature=0.6
    ).choices[0].message.content.strip()

    duaa = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": daily_duaa_prompt(day)}],
        temperature=0.6
    ).choices[0].message.content.strip()

    quran = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": daily_quran_prompt(day)}],
        temperature=0.4
    ).choices[0].message.content.strip()

    return {
        "day": day,
        "message": message,
        "duaa": duaa,
        "quran": quran
    }
