import pika
import time
import logging

# Configuração do logging para melhor depuração
logging.basicConfig(level=logging.INFO)

def connect_to_rabbitmq():
    retries = 5
    for i in range(retries):
        try:
            # Tentando conectar ao RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            logging.info("Connected to RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError:
            logging.warning(f"Retrying connection to RabbitMQ... ({i + 1}/{retries})")
            time.sleep(5)
    raise Exception("Failed to connect to RabbitMQ after several attempts.")

# Estabelecendo a conexão com RabbitMQ
connection = connect_to_rabbitmq()
channel = connection.channel()

# Declarar a fila para garantir que ela exista
channel.queue_declare(queue='notifications')

# Callback para processar as mensagens da fila
def callback(ch, method, properties, body):
    logging.info(f"Received message: {body.decode()}")
    # Aqui, você pode adicionar lógica para processar a mensagem, como enviar notificações.
    # Após o processamento, a mensagem será automaticamente confirmada com auto_ack=True.

channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)

logging.info("Waiting for messages...")
# Inicia o consumo das mensagens
channel.start_consuming()
