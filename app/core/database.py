import boto3
from app.core.config import settings


def get_table(table_name: str):
    resource = boto3.resource(
        "dynamodb",
        region_name=settings.region,
    )
    return resource.Table(table_name)
