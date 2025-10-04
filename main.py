# ===========================
# 🔹 Telegram Poster Bot + Keep Alive Server for Replit
# ===========================

import asyncio
import random
from telethon import TelegramClient, errors
from flask import Flask
from threading import Thread

# 🔸 Flask mini-server لتشغيل Replit دائمًا
app = Flask('')

@app.route('/')
def home():
    return "✅ Bot is running fine!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


# ===========================
# 🔹 إعدادات Telegram
# ===========================
api_id = 24557795
api_hash = "4fb214d957fd3e1cb04ae9d6cb7bf37e"
session_name = "poster"

messages = [
    """
    🔗 تابع حسابي على لينكدإن:
    https://www.linkedin.com/in/ahmed-ayman-2a470a381

    🤝 وشوف كمان:
    https://www.linkedin.com/in/robanzol-furoz-b50b8b387
    """,
    """
    👨‍💼 حساباتي على LinkedIn:
    - Ahmed Ayman: https://www.linkedin.com/in/ahmed-ayman-2a470a381
    - Robanzol Furoz: https://www.linkedin.com/in/robanzol-furoz-b50b8b387
    """,
    """
    ✨ تابعنا على LinkedIn للمزيد من الفرص والروابط المفيدة:
    https://www.linkedin.com/in/ahmed-ayman-2a470a381
    https://www.linkedin.com/in/robanzol-furoz-b50b8b387
    """
]

# ضع أسماء الجروبات أو القنوات هنا بدون https://t.me/
targets = [
    "LinkedIn40",
    "YourSecondGroup"
]

client = TelegramClient(session_name, api_id, api_hash)


async def main():
    await client.start()
    print("✅ تم تسجيل الدخول بنجاح. البوت يعمل الآن...\n")

    while True:
        try:
            message = random.choice(messages).strip()

            # إرسال الرسالة لكل جروب
            for target in targets:
                await client.send_message(target, message)
                print(f"🚀 تم إرسال رسالة إلى {target}")
                await asyncio.sleep(random.randint(5, 10))

            # الانتظار دقيقة واحدة فقط
            wait_time = 60
            print(f"\n⌛ الانتظار {wait_time} ثانية قبل الإرسال التالي...\n")
            await asyncio.sleep(wait_time)

        except errors.FloodWaitError as e:
            print(f"⏳ Telegram طلب الانتظار {e.seconds} ثانية.")
            await asyncio.sleep(e.seconds)
        except Exception as ex:
            print(f"⚠️ خطأ: {ex}")
            await asyncio.sleep(60)


if __name__ == "__main__":
    keep_alive()  # تشغيل السيرفر
    with client:
        client.loop.run_until_complete(main())
