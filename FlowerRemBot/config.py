# config.py

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DATABASE_NAME = os.getenv(
    "DATABASE_NAME", "bot_data.db"
)  # Можно задать значение по умолчанию
MOSCOW_TIMEZONE = os.getenv("MOSCOW_TIMEZONE", "Europe/Moscow")

# Настройки Webhook
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")  # Если используете

# Проверка наличия обязательных переменных
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN must be set")
