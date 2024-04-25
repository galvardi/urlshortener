from dataclasses import dataclass

from dynamo_db_manger import DynamoDBManager


@dataclass
class DependenciesContainer:
    db = DynamoDBManager()
