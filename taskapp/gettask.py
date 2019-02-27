#! /usr/bin/env python

"""
A lambda function to retrieve tasks stored in a dynamoDB

Test item
{
"id":"1",
}
"""
import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table_name = 'todolist'

def gettask_handler(event, context):
    """
    Get an item (task) from a dynamoDB table.

    input is an object with a task id
    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.get_item(
            TableName=table_name,
            Key={
                "id": event['id']
                }
            )
        return resp['Item']
    except Exception as e:
        print("Getting an object from table failed: {}".format(e))
