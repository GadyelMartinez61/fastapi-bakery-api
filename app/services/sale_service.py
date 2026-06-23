from app.repositories.sale_repo import SaleRepo
from app.schemas.sale import SaleCreate


class SaleService:
    def __init__(self):
        self.repo = SaleRepo()

    def get(self, branch_id: str, sale_id: str) -> dict | None:
        return self.repo.get(branch_id, sale_id)

    def create(self, data: SaleCreate) -> dict:
        return self.repo.create(data.model_dump())

    def delete(self, branch_id: str, sale_id: str) -> dict | None:
        return self.repo.delete(branch_id, sale_id)

    def list(self, limit: int = 10, last_key: str | None = None) -> dict:
        return self.repo.list(limit, last_key)
