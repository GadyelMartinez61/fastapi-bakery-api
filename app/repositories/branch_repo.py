from app.core.database import get_table
from app.core.config import settings
from uuid import uuid4
from datetime import datetime, timezone
from botocore.exceptions import ClientError

DATABASE = get_table(settings.branches_table)


class BranchRepo:
    def get(self, branch_id: str) -> dict | None:
        response = DATABASE.get_item(Key={"id": branch_id})
        return response.get("Item")

    def create(self, data: dict) -> dict:
        item = {
            "id": uuid4().hex,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": None,
            **data,
        }
        DATABASE.put_item(Item=item)
        return item

    def delete(self, branch_id: str) -> dict | None:
        item = self.get(branch_id)
        if not item:
            return None
        try:
            DATABASE.delete_item(Key={"id": branch_id})
        except ClientError:
            return None

        return item

    def list(self, limit: int = 10, last_key: str | None = None) -> dict:
        kwargs = {"Limit": limit}
        if last_key:
            kwargs["ExclusiveStartKey"] = {"id": last_key}

        response = DATABASE.scan(**kwargs)
        items = response.get("Items", [])
        last_evaluated_key = response.get("LastEvaluatedKey")

        return {
            "items": items,
            "last_key": last_evaluated_key["id"] if last_evaluated_key else None,
            "count": len(items),
        }
