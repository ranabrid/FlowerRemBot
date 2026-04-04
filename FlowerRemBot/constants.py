# constants.py

from telegram.ext import ConversationHandler

# Состояния для ConversationHandler
STATUS_CHECK, AWAITING_ANSWER, CHOOSING_DATE = range(3)
CHOOSING_INTERVAL, CUSTOM_INTERVAL = 3, 4
# Callback-данные для кнопок
CALLBACK_PLAN = "plan"
CALLBACK_LATER = "later"
CALLBACK_BOUGHT = "bought"
CALLBACK_HOUR_LATER = "hour_later"
CALLBACK_DAY_LATER = "day_later"
CALLBACK_SCHEDULE_YES = "schedule_yes"
CALLBACK_SCHEDULE_NO = "schedule_no"
MOSCOW_TIMEZONE = "Europe/Moscow"
# Сообщения (можно перенести сюда все)
MSG_WELCOME_START = "🌷 Привет! Я буду напоминать тебе купить цветы"
MSG_PLAN_DATE = "Когда ты хочешь получить напоминание?"
MSG_POSTPONED_MESSAGE = "Хорошо, отправь /start, когда передумаешь"
MSG_BOUGHT_SUCCESS = "💫Молодец!"
MSG_REMINDER_TEXT = "🌷Пора купить цветы!🌷"
MSG_DELIVERY_URL = (
    "https://yandex.ru/search/?text=доставка+цветов&clid=2411726&lr=21651"
)
MSG_INVALID_DATE_INPUT = "🧐Не могу распознать дату. Попробуй ввести ее снова, например, 'завтра' или '15 мая'."
MSG_REMINDER_SCHEDULED_SUCCESS = "Напоминание запланировано на {date}!"
MSG_CANCEL_SUCCESS = "⚠️Все напоминания были отменены. Если понадобится новое расписание, то просто отправь мне /start 🌼"
MSG_REMINDER_ALREADY_ACTIVE = (
    "Для тебя уже запланировано напоминание на {date}. Хочешь его изменить?"
)
MSG_NO_ACTIVE_REMINDER = "Запланированных напоминаний нет. Запланировать?"
MSG_KEEP_REMINDER = "Хорошо, напоминание придёт по запланированному расписанию"
MSG_HOUR_REMINDER = "Хорошо, напомню через час"
MSG_DAY_REMINDER = "Хорошо, напомню завтра"
MSG_OLD_DATE = "🟠Введено время в прошлом. Пожалуйста, укажи дату и время в будущем."
MSG_ASK_INTERVAL = "Хочешь, буду напоминать регулярно? Выбери как часто 🌸"
