import boto3


class DynamoDBManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.table = boto3.resource('dynamodb')

    def add_long_url(long_url: str, url_hash: str):
        self.table.
