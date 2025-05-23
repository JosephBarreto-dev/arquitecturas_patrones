import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='correos')

mensaje = {
    "para": "paquito@gmail.com",
    "asunto": "Gracias por tu compra!",
    "cuerpo": "Tu pedido ha sido recibido. gracias por confiar en nosotros!"
}

channel.basic_publish(exchange='',
                      routing_key='correos',
                      body=json.dumps(mensaje))

print("solicitud de envío enviada.")
connection.close()
