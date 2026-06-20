from app.core.config import settings
from app.core.database import get_table
from botocore.exceptions import ClientError
from datetime import datetime, timezone


DATABASE = get_table(settings.users_table)


class UserRepo:
    def get(self, username: str) -> dict | None:
        response = DATABASE.get_item(Key={"username": username})
        return response.get("Item")

    def create(self, data: dict) -> dict:
        item = {
            **data,
            "is_active": True,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": None,
        }
        DATABASE.put_item(Item=item)

        return item

    def update(self, username: str, data: dict) -> dict:
        old_item = self.get(username)

        merged = {
            **old_item,
            **data,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }

        DATABASE.put_item(Item=merged)

        return merged

    def delete(self, username: str) -> dict | None:
        item = self.get(username)
        if not item:
            return None
        try:
            DATABASE.delete_item(
                Key={
                    "username": username,
                }
            )
        except ClientError:
            return None

        return item

    def list(self, limit: int = 10, last_key: str | None = None) -> dict:
        kwargs = {"Limit": limit}
        if last_key:
            kwargs["ExclusiveStartKey"] = {"username": last_key}

        response = DATABASE.scan(**kwargs)
        items = response.get("Items", [])
        last_evaluated_key = response.get("LastEvaluatedKey")

        return {
            "items": items,
            "last_key": last_evaluated_key["username"] if last_evaluated_key else None,
            "count": len(items),
        }
