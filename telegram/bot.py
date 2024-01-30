from aiogram import Bot, Dispatcher

from config import Settings
from .database import manager
from .services import WelcomeRouter, SenderRouter


class Telegram:
    _bot: Bot = Bot(token=Settings.TG_TOKEN)
    _dp: Dispatcher = Dispatcher()

    @classmethod
    async def start(cls) -> None:
        cls._dp.include_routers(WelcomeRouter, SenderRouter)
        cls._dp.startup.register(cls.onstartup)
        await cls._dp.start_polling(cls._bot)

    @staticmethod
    async def onstartup() -> None:
        await manager.connect()
