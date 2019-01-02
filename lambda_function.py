import json

def lambda_handler(event, context):
    body = {
        'sequence': event['sequence'], 
        'k': event['k']
    }
    
    return {
        'statusCode': 200,
        'body': body
    }
