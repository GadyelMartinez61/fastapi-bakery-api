from app.repositories.branch_repo import BranchRepo
from app.schemas.branch import BranchCreate, BranchUpdate


class BranchService:
    def __init__(self):
        self.repo = BranchRepo()

    def get(self, branch_id: str) -> dict | None:
        return self.repo.get(branch_id)

    def create(self, data: BranchCreate) -> dict:
        return self.repo.create(data.model_dump())

    def update(self, branch_id: str, data: BranchUpdate) -> dict | None:
        existing = self.repo.get(branch_id)
        if not existing:
            return None
        return self.repo.update(branch_id, data.model_dump(exclude_unset=True))

    def delete(self, branch_id: str) -> dict | None:
        return self.repo.delete(branch_id)

    def list(self, limit: int = 10, last_key: str | None = None) -> dict:
        return self.repo.list(limit, last_key)
