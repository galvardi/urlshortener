from abc import ABC
from typing import Optional

import boto3

from constants import LONG_TO_SHORT_DB_NAME, SHORT_TO_LONG_DB_NAME, HASHED_URL, LONG_URL, AWS_DEFAULT_REGION


# for mock class later
class DynamoDBManagerInterface(ABC):
    def add_url(self, key: str, value: str):
        raise NotImplementedError

    def get_url(self, key: str):
        raise NotImplementedError


class DynamoDBManager:
    def __init__(self):
        self.long_to_short_table = boto3.resource('dynamodb', region_name=AWS_DEFAULT_REGION).Table(LONG_TO_SHORT_DB_NAME)
        self.short_to_long_table = boto3.resource('dynamodb', region_name=AWS_DEFAULT_REGION).Table(SHORT_TO_LONG_DB_NAME)

    def add_url(self, key: str, value: str):
        if self.get_url(key=key): return
        self.long_to_short_table.put_item(Item={LONG_URL: key, HASHED_URL: value})
        self.short_to_long_table.put_item(Item={HASHED_URL: key, LONG_URL: value})

    def get_url(self, key: str) -> Optional[str]:
        response = self.short_to_long_table.get_item(Key={HASHED_URL: key})
        if not response.get("Item"): return
        return response["Item"][LONG_URL]

# if __name__ == '__main__':
#     manager = DynamoDBManager()
#     print(manager.add_url("youtubeg.com", "asdasdkkss"))
#     print(manager.add_url("youtubeg.com", "asadasdkkss"))
#     print(manager.get_url("youtube.com"))
#     print(manager.get_url("youske.com"))
