#! /usr/bin/env python

"""
A lambda function to add a task to a dynamoDB

Create the dynamoDB instance locally to test functionality
"""
import boto3

#dynamodb = boto3.resource('dynamodb',  endpoint_url="http://localhost:8000")  # local test
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
client = boto3.client('dynamodb')
table_name = 'todolist'
# Table already created successfully in first run. TODO: If table
# exists raise an exception to that effect.
def handler(event, context):
    """
    Add a task to a dynamoDB table.
    
    Expects input in the following format in lambda testing environment
    {
    "id": "1",
    "name: New task"
    }

    Note: POST requests pass a body and not queryStringParameters
    """
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                    },
                ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                    },
                ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
                }
            )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        try:
            resp = table.put_item(
                Item=event["body"]
                )
        except Exception as e:
            print ("Writing to table failed with error: {}".format(e))
    except client.exceptions.ResourceInUseException:
        table = dynamodb.Table(table_name)
        try:
            resp = table.put_item(
                Item=event["body"],
                ReturnValues='NONE'
                )
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin" : "*",
                },
                "body": json.dumps(resp)
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                    },
                "body": json.dumps(str(e))
               }
