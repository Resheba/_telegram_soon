import logging
from asyncio import run

from telegram import Telegram
from telegram.database import User, manager


logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    run(Telegram.start())
