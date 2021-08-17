from kombu import Connection, Consumer, Exchange, Queue, eventloop

queueName = "/mining/inference/v1/status/reply"
exchange = Exchange(queueName, type='direct')
queue = Queue(queueName, exchange, routing_key=queueName)

def handle_message(body, message):
    print(f'Received message: {body!r}')
    message.ack()


with Connection('amqp://guest:guest@localhost:5672//') as connection:
    with Consumer(connection, queue, callbacks=[handle_message]):
        for _ in eventloop(connection):
            pass