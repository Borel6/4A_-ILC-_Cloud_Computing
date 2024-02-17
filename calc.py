#!/usr/bin/env python
import pika, sys, os 
import json
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

def main() :


    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='calculs')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        operation = message['message']['op']
        numA = message['message']['numA']
        numB = message['message']['numB']
        id = message['id']

        #if (operation == "add") :
            #C = int(numA) + int(numB)
            #r.set(id, C) 
        if (operation == "subs") :
            C = int(numA) - int(numB)
            r.set(id, C) 
        if (operation == "div") :
            C = int(numA) / int(numB)
            r.set(id, C) 
        if (operation == "multi") :
            C = int(numA) * int(numB)
            r.set(id, C) 

        print(f" [x] Received {body}")

    channel.basic_consume(queue='calculs',
                        auto_ack=True,
                        on_message_callback=callback)


    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)