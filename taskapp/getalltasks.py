"""
A lambda function to fetch all tasks from a dynamoDB

Expected output:

{
    "tasks": [
        {
            "id": "1",
            "name": "New task",
            "done": true
        },
        {
            "id": "2",
            "name": "Another task",
            "done": false
        }
    ]
}
"""
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table_name = 'todolist'

def fetchAll_handler(event, context):
    """
    Fetch all tasks in the dynamoDB table
    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.scan(
            TableName=table_name
            )
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin" : "*",
            },
            "body": json.dumps(resp["Items"])
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": '*'
                },
            "body": json.dumps(str(e))
            }
