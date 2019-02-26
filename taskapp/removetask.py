"""
A lambda function to remove an object from a DynamoDB

Expected input:

{
    "id": "2"
}
"""
import boto3

dynamodb = boto3.resource('dynamodb')  # endpoint_url="http://localhost:8000
client = boto3.client('dynamodb')

def removeTask_handler(event, context):
    """
    Remove a task in the dynamoDB table

    """
    try:
        resp = client.delete_item(
            TableName='todolist',
            Key={
                "id": event["id"]
                }
            )
    except Exception as e:
        print("Removing task id: {} failed: {}".format(event["id"], e))
