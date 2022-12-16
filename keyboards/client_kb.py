from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    # one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
mems_button = KeyboardButton("/mems")

share_location = KeyboardButton("Отправить локацию", request_location=True)
share_contact = KeyboardButton("Отправить контакт", request_contact=True)

start_markup.add(start_button, help_button, quiz_button, mems_button, share_location, share_contact)