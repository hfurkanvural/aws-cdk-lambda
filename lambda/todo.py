import utils
import json
import boto3
import os
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

def get(event, context):
    table = dynamodb.Table(TABLE_NAME)
    id = event.get('pathParameters').get('todoId')
    try:
        response = table.get_item(
        Key={
            'id': id
        }
    )
    except ClientError as e:
        return utils.respond_error()
    else:
        if 'Item' in response:
            return utils.respond_success(response['Item'])
        else:
            return utils.respond_not_found({"error":"ToDo could not be found."})


def put(event, context):
    data = json.loads(event.get('body'))
    table = dynamodb.Table(TABLE_NAME)
    id = str(uuid.uuid4())
    response = table.put_item(
            Item={
                'id': id,
                'task': data['todo']
            }
        )
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return utils.respond_success({"result":"succesfully added."})
    else:
        return utils.respond_not_found({"error":"ToDo could not be found."})
    

def delete(event, context):
    table = dynamodb.Table(TABLE_NAME)
    id = event.get('pathParameters').get('todoId')
    try:
        response = table.delete_item(
        Key={
            'id': id
        }
    )
    except ClientError as e:
        return utils.respond_error()
    else:
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return utils.respond_success({"result":"succesfully deleted."})
        else:
            return utils.respond_not_found({"error":"ToDo could not be found."})
