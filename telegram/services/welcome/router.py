from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ...database import UserRepository


router: Router = Router(name='Welcome')


@router.message(Command('start'))
async def start_command(message: Message):
    if await UserRepository.is_registred(message.from_user.id):
        await message.answer('Hi, asshole!)')
    else:
        await UserRepository.register(id=message.from_user.id)
        await message.answer('First time? Dont worry)')
    