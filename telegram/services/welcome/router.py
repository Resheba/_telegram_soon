from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router: Router = Router(name='Welcome')


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Hi, asshole!)')
    