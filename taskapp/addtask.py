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
    "id": {"S": "1"},
    "name: {"S": "New task"}
    }
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
        print(">>> Table item count {}".format(table.item_count))
        for record in event:
            try:
                resp = table.put_item(
                    TableName=table_name,
                    Item=record
                    )
            except Exception as e:
                print ("Writing to table failed with error: {}".format(e))
    except client.exceptions.ResourceInUseException:
        table = dynamodb.Table(table_name)
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print(">>> Table item count {}".format(table.item_count))
        for record in event:
            try:
                resp = table.put_item(
                    TableName=table_name,
                    Item=record
                    )
            except Exception as e:
                print ("Writing to table failed with error: {}".format(e))
