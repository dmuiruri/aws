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

dynamodb = boto3.resource('dynamodb')
table_name = 'todolist'

def updateTaskStatus_handler(event, context):
    """
    Update an item (task) in dynamoDB table.

    input is an object with a task id and other attributes to be
    updated.
    """
    table = dynamodb.Table(table_name)
    key={"id": event["queryStringParameters"]["id"]}
    try:
        resp = table.update_item(
            Key=key,
            UpdateExpression='SET done = :val1',
            ExpressionAttributeValues={':val1': event["queryStringParameters"]["done"]}
            )
        return{
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin" : "*",},
            "body": json.dumps(resp)
        }
    except Exception as e:
        print("Updating a task failed: {}".format(e))
