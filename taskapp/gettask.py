#! /usr/bin/env python

"""
A lambda function to retrieve tasks stored in a dynamoDB

Test item
{
"id":"1",
}
"""
import boto3
import json

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table_name = 'todolist'

def gettask_handler(event, context):
    """
    Get an item (task) from a dynamoDB table.

    input is an object with a task id.

    The API Gateway has a request body item that contains the
    parameters to be passed to the API endpoint, the object is already
    a dictionary which we can pass to dynamoDB.

    In order for API Gateway to actually deliver the output, the
    returned object has to contain at least a statusCode and a
    body. The returned object should look like:
    {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin" : "*",
    },
    "body": <return value as a JSON string>
    }
    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.get_item(
            TableName=table_name,
            Key=event['requestStringParameters']
            )
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin" : "*",
                },
            "body": json.dumps(resp["Item"]) # <return value as a JSON string>
            }
    except Exception as e:
        print("Getting an object from table failed: {}".format(e))
