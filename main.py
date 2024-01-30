import logging
from asyncio import run

from telegram import Telegram
from rabbitmq import RabbitClient


logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    RabbitClient.start()
    run(Telegram.start())
