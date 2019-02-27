#! /usr/bin/env python

"""
A lambda function to update an object in DynamoDB

Test item
{
"id":  "1",
"done": true
}
"""
import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table_name = 'todolist'

def updateTaskStatus_handler(event, context):
    """
    Update an item (task) in dynamoDB table.

    input is an object with a task id
    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.update_item(
            TableName=table_name,
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
