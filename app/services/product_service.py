from app.repositories.product_repo import ProductRepo
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self):
        self.repo = ProductRepo()

    def get(self, branch_id: str, product_id: str) -> dict | None:
        return self.repo.get(branch_id, product_id)

    def create(self, data: ProductCreate) -> dict:
        return self.repo.create(data.model_dump())

    def update(self, branch_id: str, product_id: str, data: ProductUpdate) -> dict | None:
        existing = self.repo.get(branch_id, product_id)
        if not existing:
            return None
        return self.repo.update(branch_id, product_id, data.model_dump(exclude_unset=True))

    def delete(self, branch_id: str, product_id: str) -> dict | None:
        return self.repo.delete(branch_id, product_id)

    def list(self, limit: int = 10, last_key: str | None = None) -> dict:
        return self.repo.list(limit, last_key)
