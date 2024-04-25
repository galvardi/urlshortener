import boto3


class DynamoDBManager:
    def __init__(self):
        # self.table_name = table_name
        self.db = boto3.resource('dynamodb')

    def add_to_table(self, table_name: str, key: str, value: str):
        table = self.db.Table(table_name)
        table.put_item(Item={"long_url":key, "hashed_url":value})

    def get_from_table(self,table_name: str, key):
        table = self.db.Table(table_name)
        response = table.get_item(Key={"long_url":key})
        if not response.get("Item"): return None
        return response["Item"]["hashed_url"]

if __name__ == '__main__':
    manager = DynamoDBManager()
    print(manager.add_to_table("long-to-short","youtube.com", "akkss"))
    print(manager.get_from_table("long-to-short", "youtube.com"))
    print(manager.get_from_table("long-to-short", "youske.com"))