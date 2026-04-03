import logging
from config import TELEGRAM_BOT_TOKEN
from handlers import setup_bot
from database import init_db

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():

    if not TELEGRAM_BOT_TOKEN:
        logger.error("Токен бота не найден. Пожалуйста, укажите его в файле .env")
        return

    # 1. Инициализируем базу данных
    init_db()

    # 2. Создаем объект Application
    from telegram.ext import ApplicationBuilder

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # 3. Настраиваем обработчики
    setup_bot(application)

    # 4. Запускаем бота.

    logger.info("Бот запущен! Работает через Polling.")

    try:
        application.run_polling()
    except AttributeError:

        application.start_polling()
        application.idle()


if __name__ == "__main__":
    main()
