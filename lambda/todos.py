import utils
import json
import boto3
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

def get(event, context):
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()

    return utils.respond_success(response['Items'])    
