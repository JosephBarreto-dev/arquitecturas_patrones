import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='viajes')

def callback(ch, method, properties, body):
    evento = json.loads(body)
    print(f"notificando usuario {evento['usuario_id']} que el conductor {evento['conductor_id']} aceptó el viaje {evento['viaje_id']}.")

channel.basic_consume(queue='viajes',
                      on_message_callback=callback,
                      auto_ack=True)

print('Esperando eventos..')
channel.start_consuming()
