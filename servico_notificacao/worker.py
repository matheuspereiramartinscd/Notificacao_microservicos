import pika
import time


def connect_to_rabbitmq():
    retries = 5
    for i in range(retries):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            print("Connected to RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"Retrying connection to RabbitMQ...")
            time.sleep(5)
    raise Exception("Failed to connect to RabbitMQ after several attempts.")

connection = connect_to_rabbitmq()
channel = connection.channel()

# Declare a queue to ensure it exists
channel.queue_declare(queue='notifications')

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)

print("Waiting for messages...")
channel.start_consuming()
