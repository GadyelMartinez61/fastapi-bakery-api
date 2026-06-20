from app.core.config import settings
from botocore.exceptions import ClientError
from app.core.database import get_table
from uuid import uuid4
from datetime import datetime, timezone


DATABASE = get_table(settings.sales_table)


class SaleRepo:
    def get(self, branch_id: str, sale_id: str) -> dict | None:
        response = DATABASE.get_item(Key={"branch_id": branch_id, "sale_id": sale_id})
        return response.get("Item")

    def create(self, data: dict) -> dict:
        item = {
            "sale_id": uuid4().hex,
            "branch_id": data["branch_id"],
            "is_active": True,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": None,
            **data,
        }
        DATABASE.put_item(Item=item)
        return item

    def update(self, branch_id: str, sale_id: str, data: dict) -> dict:
        old_item = self.get(branch_id, sale_id)

        merged = {
            **old_item,
            **data,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }

        DATABASE.put_item(Item=merged)

        return merged

    def delete(self, branch_id: str, sale_id: str) -> dict | None:
        item = self.get(branch_id, sale_id)
        if not item:
            return None
        try:
            DATABASE.delete_item(Key={"branch_id": branch_id, "sale_id": sale_id})
        except ClientError:
            return None

        return item

    def list(self, limit: int = 10, last_key: dict | None = None) -> dict:
        kwargs = {"Limit": limit}
        if last_key:
            kwargs["ExclusiveStartKey"] = last_key

        response = DATABASE.scan(**kwargs)
        items = response.get("Items", [])
        last_evaluated_key = response.get("LastEvaluatedKey")

        return {
            "items": items,
            "last_key": last_evaluated_key if last_evaluated_key else None,
            "count": len(items),
        }
