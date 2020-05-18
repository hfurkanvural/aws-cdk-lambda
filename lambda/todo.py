import utils
import json
import boto3

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

def get(event, context):
    table = dynamodb.Table(TABLE_NAME)
    id = event.get('pathParameters').get('id')
    try:
        response = table.get_item(
        Key={
            'id': id
        }
    )
    except ClientError as e:
        return utils.respond_success(e.response['Error']['Message'])
    else:
        return utils.respond_success(response['Item'])


def put(event, context):
    table = dynamodb.Table(TABLE_NAME)
    response = table.put_item(
            Item={
                'id': event['id'],
                'task': event['todo']
            }
        )
    
    return  utils.respond_success(response)
    

def delete(event, context):
    table = dynamodb.Table(TABLE_NAME)
    id = event.get('pathParameters').get('id')
    try:
        response = table.delete_item(
        Key={
            'id': id
        }
    )
    except ClientError as e:
        return utils.respond_success(e.response['Error']['Message'])
    else:
        return utils.respond_success(response['Item'])
