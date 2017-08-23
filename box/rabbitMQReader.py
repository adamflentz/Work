#!/usr/bin/env python

import pika

parameters = pika.URLParameters(
    'amqps://aflentz:$284233Vb@mq-test-00.it.wm.edu/jason_test')  # Jason_test is the virtual host

connection = pika.BlockingConnection(parameters)

ch = connection.channel()

ch.queue_declare(queue='hello', durable=True)  # hello is the queue


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


ch.basic_consume(callback,

                 queue='hello',

                 no_ack=True)

# print datetime.datetime.now()

print(' [*] Waiting for messages. To exit press CTRL+C -- ')

ch.start_consuming()

