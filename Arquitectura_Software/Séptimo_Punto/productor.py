import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='viajes')
evento = {
    "evento": "viaje_aceptado",
    "viaje_id": "12345",
    "conductor_id": "C789",
    "usuario_id": "U456"
}
channel.basic_publish(exchange='',
                      routing_key='viajes',
                      body=json.dumps(evento))

print("Evento enviado: viaje_aceptado")
connection.close()
