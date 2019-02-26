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

dynamodb = boto3.resource('dynamodb')  # endpoint_url="http://localhost:8000
client = boto3.client('dynamodb')

def fetchAll_handler(event, context):
    """
    Fetch all tasks in the dynamoDB table

    """
    try:
        resp = client.scan(
            TableName='todolist'
            )
    except Exception as e:
        print("Fetching all tasks failed: {}".format(e))
