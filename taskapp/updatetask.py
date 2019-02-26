#! /usr/bin/env python

"""
A lambda function to update an object in DynamoDB

Test item
{
"id": {"S": "1"},
"done": {"BOOL": true}
}
"""
import boto3

dynamodb = boto3.resource('dynamodb')  # endpoint_url="http://localhost:8000
client = boto3.client('dynamodb')

def updateTaskStatus_handler(event, context):
    """
    Update an item (task) in dynamoDB table.

    input is an object with a task id
    """
    try:
        resp = client.update_item(
            TableName='todolist',
            Key={
                "id": event['id']
                },
            UpdateExpression='SET done = :val1',
            ExpressionAttributeValues={
                ':val1': event["done"]
                }
            )
    except Exception as e:
        print("Updating a task failed: {}".format(e))
