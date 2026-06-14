from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    detail: str


class PaginatedResponse(BaseModel):
    items: list
    count: int
    next_key: str | None = None
