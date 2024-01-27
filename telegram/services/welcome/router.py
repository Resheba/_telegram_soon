from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from ...database import UserRepository
from .keyboard import TimeKeyboard, TimeCallback
from .utils import get_time


router: Router = Router(name='Welcome')


@router.message(Command('start'))
async def start_command(message: Message):
    if await UserRepository.is_registred(message.from_user.id):
        await message.answer('Time?', reply_markup=TimeKeyboard.keyboard)
    else:
        await UserRepository.register(id=message.from_user.id)
        await message.answer('First time? Dont worry)')


@router.callback_query(TimeCallback.filter())
async def time_callback(query: CallbackQuery, callback_data: TimeCallback):
    await query.answer(await get_time(callback_data.city), show_alert=True)
    