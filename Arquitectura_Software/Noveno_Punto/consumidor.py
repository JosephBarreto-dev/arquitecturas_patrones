import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='correos')

def enviar_correo(mensaje):
    print(f"""
     Enviando correo a: {mensaje['para']}
     Asunto: {mensaje['asunto']}
     Cuerpo: {mensaje['cuerpo']}
""")
    time.sleep(2)  # Simula el tiempo de envío
    print("Correo enviado.\n")

def callback(ch, method, properties, body):
    mensaje = json.loads(body)
    enviar_correo(mensaje)

channel.basic_consume(queue='correos',
                      on_message_callback=callback,
                      auto_ack=True)

print('Esperando correos para enviar')
channel.start_consuming()
