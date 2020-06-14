import json

def lambda_handler(event, context):
    print('This is a test')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
