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
import json

dynamodb = boto3.resource('dynamodb')
table_name = 'todolist'

def updateTaskStatus_handler(event, context):
    """
    Update an item (task) in dynamoDB table.

    input is an object with a task id and other attributes to be
    updated.
    """
    table = dynamodb.Table(table_name)
    obj = json.loads(event["body"])
    try:
        resp = table.get_item(Key={"id": obj["id"]}).keys()
        if 'Item' in resp:
            resp = table.update_item(
                Key={"id": obj["id"]},
                UpdateExpression='SET done = :val1',
                ExpressionAttributeValues={':val1': obj["done"]}
                )
            return {
                "statusCode": 200,
                "headers": {"Access-Control-Allow-Origin": "*",},
                "body": json.dumps(resp)
                }
        else:
            return {
                "statusCode": 200,
                "headers": {"Access-Control-Allow-Origin": "*",},
                "body": json.dumps("Item doesn't exist")
                }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
                },
            "body": json.dumps(str(e))
            }
