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
table_name = 'todolist'

def gettask_handler(event, context):
    """
    Get an item (task) from a dynamoDB table.

    input is an object with a task id.

    The API Gateway delivers GET requests and a POST body to the
    lambda functions within lambda's event object. The events object
    contains the entire Endpoint request body containing objects such
    as
    "queryStringParameters":{"id":"2"},"multiValueQueryStringParameters"
    etc.

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
    key = event['queryStringParameters']
    try:
        resp = table.get_item(
            Key=key
            )
        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin" : "*",},
            "body": json.dumps(resp["Item"])
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers" {
                "Access-Control-Allow-Origin": '*'
                }
            "body": json.dumps(str(e))
            }
