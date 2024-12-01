import pika

from flask import Flask, request, jsonify

app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare a queue to ensure it exists
channel.queue_declare(queue='notifications')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    message = data.get('message', 'No message provided')
    channel.basic_publish(exchange='', routing_key='notifications', body=message)
    return jsonify({"status": "Notification queued"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
