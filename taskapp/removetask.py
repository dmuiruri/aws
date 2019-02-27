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
table_name = 'todolist'

def removeTask_handler(event, context):
    """
    Remove a task in the dynamoDB table

    """
    table = dynamodb.Table(table_name)
    try:
        resp = table.delete_item(
            TableName=table_name,
            Key={
                "id": event["id"]
                }
            )
        return resp
    except Exception as e:
        print("Removing task id: {} failed: {}".format(event["id"], e))
