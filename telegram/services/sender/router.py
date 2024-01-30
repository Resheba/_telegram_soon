from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji

from rabbitmq import RabbitClient


router: Router = Router(name='Sender')


@router.message(Command('send'))
async def send_command(message: Message, command: CommandObject):
    text: str = command.args
    if not text:
        await message.answer('/send <text>')
        return
    
    RabbitClient.publish(message=text, user_id=message.from_user.id)

    await message.react(reaction=[ReactionTypeEmoji(emoji='👍')], is_big=False)
    