"""
A lambda function to remove an object from a DynamoDB

Expected input:

{
    "id": "2"
}
"""
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table_name = 'todolist'

def removeTask_handler(event, context):
    """
    Remove a task in the dynamoDB table

    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.delete_item(
            TableName=table_name,
            Key=event["queryStringParameters"]
            )
        return {
            "statusCode":200,
            "headers": {"Access-Control-Allow-Origin" : "*",},
            "body": json.dumps(resp)
        }
    except Exception as e:
        print("Removing task failed: {}".format(e))
