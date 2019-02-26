#! /usr/bin/env python

"""
A lambda function to retrieve tasks stored in a dynamoDB

Test item
{"id": {"S": "1"}}
"""
import boto3

dynamodb = boto3.resource('dynamodb')  # endpoint_url="http://localhost:8000
client = boto3.client('dynamodb')

def gettask_handler(event, context):
    """
    Get an item (task) from a dynamoDB table.

    input is an object with a task id
    """
    try:
        resp = client.get_item(
            TableName='todolist',
            Key={
                "id": event['id']
                }
            )
    except Exception as e:
        print("Getting an object from table failed: {}".format(e))
