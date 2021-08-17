from kombu import Connection, Consumer, Exchange, Queue, eventloop
from dotenv import load_dotenv
import os

load_dotenv()

queueName = "/mining/inference/v1/status/reply"
exchange = Exchange(queueName, type='direct')
queue = Queue(queueName, exchange, routing_key=queueName)

def handle_message(body, message):
    print(f'Received message: {body!r}')
    message.ack()


with Connection(os.getenv("RABBITMQ_HOST")) as connection:
    with Consumer(connection, queue, callbacks=[handle_message]):
        for _ in eventloop(connection):
            pass