from aiogram import Bot, Dispatcher

from config import Settings
from .services import WelcomeRouter


class Telegram:
    _bot: Bot = Bot(token=Settings.TG_TOKEN)
    _dp: Dispatcher = Dispatcher()

    @classmethod
    async def start(cls) -> None:
        cls._dp.include_routers(WelcomeRouter)
        await cls._dp.start_polling(cls._bot)
