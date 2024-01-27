from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class TimeCallback(CallbackData, prefix='time'):
    city: str


class TimeKeyboard:
    get_time_button: InlineKeyboardButton = InlineKeyboardButton(text='Вермя', callback_data=TimeCallback(city='Europe/Moscow').pack())

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[get_time_button]])
