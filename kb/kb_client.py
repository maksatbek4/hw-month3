from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/anime")
quiz_1_button = KeyboardButton("/breakfast")

start_markup.add(start_button, info_button, quiz_button, quiz_1_button)

