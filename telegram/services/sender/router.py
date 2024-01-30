from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from rabbitmq import RabbitClient


router: Router = Router(name='Sender')


@router.message(Command('send'))
async def send_command(message: Message, command: CommandObject):
    text: str = command.args
    if text is None:
        await message.answer('/send <text>')
        return
    
    RabbitClient.publish(message=text, user_id=message.from_user.id)

    await message.reply_sticker(sticker='CAACAgIAAxkBAAELR5ZluIp3NmAanO3G5hKfjj-80oHRTgACYgEAAiI3jgRUwxgqIX5s5DQE')
    