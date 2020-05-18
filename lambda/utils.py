import json

def respond_success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/json'
        },
        'body': json.dumps(body)
    }

def respond_not_found(body):
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'text/json'
        },
        'body': json.dumps(body)
    }
