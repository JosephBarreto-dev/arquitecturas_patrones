import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['COMMENTS_TABLE'])

def lambda_handler(event, context):
    data = json.loads(event['body'])
    comentario = {
        'id': data['id'],
        'cliente': data['cliente'],
        'mensaje': data['mensaje'],
        'fecha': datetime.utcnow().isoformat()
    }

    table.put_item(Item=comentario)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Comentario recibido'})
    }
