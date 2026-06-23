from pydantic import BaseModel, Field, PositiveFloat, ConfigDict
from enum import Enum


class ProductCategory(str, Enum):
    cake = "Pastel"
    pastry = "Pan Dulce"
    cookie = "Galleta"


class ProductCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: PositiveFloat = Field(...)  # > 0
    category: ProductCategory
    branch_id: str


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: PositiveFloat | None = None
    category: ProductCategory | None = None
    is_active: bool | None = None


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # permite crear desde dict

    id: str
    name: str
    description: str | None
    price: float
    category: ProductCategory
    branch_id: str
    is_active: bool
    created_at: str
    updated_at: str | None
