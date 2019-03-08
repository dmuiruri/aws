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
    obj = json.loads(event['body'])
    try:
        resp = table.get_item(Key={"id": obj["id"]}).keys()
        if 'Item' in resp:
            resp = table.delete_item(
                TableName=table_name,
                Key=json.loads(event["body"])
                )
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin" : "*"
                    },
                "body": json.dumps(resp)
                }
        else:
            return {
                "statusCode": 200,
                "headers": {"Access-Control-Allow-Origin": "*",},
                "body": json.dumps("Item does not exist")
                }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
                },
            "body": json.dumps(str(e))
            }
