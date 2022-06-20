import pika
import time

i = 0

while 1:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    i += 1

    channel.basic_publish(exchange='', routing_key='hello', body='It was a massive pain to get rabbit mq working: ' + str(i))
    print(" [x] Sent 'It was a massive pain to get rabbit mq working: " + str(i) + "'")
    connection.close()
    time.sleep(1)
