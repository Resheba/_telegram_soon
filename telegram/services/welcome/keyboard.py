from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class TimeCallback(CallbackData, prefix='time'):
    city: str


class TimeKeyboard:
    moscow_button: InlineKeyboardButton = InlineKeyboardButton(text='Moscow', callback_data=TimeCallback(city='Europe/Moscow').pack())
    berlin_button: InlineKeyboardButton = InlineKeyboardButton(text='Berlin', callback_data=TimeCallback(city='Europe/Berlin').pack())
    paris_button: InlineKeyboardButton = InlineKeyboardButton(text='Tokyo', callback_data=TimeCallback(city='Asia/Tokyo').pack())

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[moscow_button, berlin_button, paris_button]])
