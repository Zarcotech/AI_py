import json
import sys
sys.path.append('../../')

from chatbot import predict_class, get_response, intents

def handler(event, context):
    try:
        user_message = json.loads(event['body'])['user_message']
        intents_list = predict_class(user_message)
        response = get_response(intents_list, intents)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': response}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
