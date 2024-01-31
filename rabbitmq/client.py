from config import Settings

from pika import BlockingConnection, URLParameters, ConnectionParameters
from pika.exchange_type import ExchangeType
from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import StreamLostError

class RabbitClient:
    _connection: BlockingConnection
    _channel: BlockingChannel

    _message_queue_name: str = 'users'
    _message_topic_name: str = 'users_topic'

    @classmethod
    def start(cls) -> None:
        cls._connect()
        cls._channel.exchange_declare(exchange=cls._message_topic_name, exchange_type=ExchangeType.topic)
        cls._channel.queue_declare(queue=cls._message_queue_name)
        cls._channel.queue_bind(queue=cls._message_queue_name, exchange=cls._message_topic_name, routing_key='user.*')
    
    @classmethod
    def publish(cls, message: str, *, user_id: int | str) -> None:
        try:
            cls._send(message=message, user_id=user_id)
        except StreamLostError:
            cls._connect()
            cls._send(message=message, user_id=user_id)
    
    @classmethod
    def _send(cls, message: str, user_id: int | str) -> None:
        cls._channel.basic_publish(exchange=cls._message_topic_name,
                                    routing_key=f'user.{user_id}',
                                    body=message)

    @classmethod
    def _connect(cls) -> None:
        cls._connection: BlockingConnection = BlockingConnection(
            [
                URLParameters(url=Settings.RABBITMQ_DSN),
                ConnectionParameters(heartbeat=10)
            ]
        )
        cls._channel: BlockingChannel = cls._connection.channel()
