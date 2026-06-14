from pydantic import BaseModel, Field, PositiveFloat
from enum import Enum


class PaymentMethod(str, Enum):
    cash = "EFECTIVO"
    card = "TARJETA"
    transfer = "TRANSFERENCIA"


class SaleItem(BaseModel):
    product_id: str
    product_name: str
    quantity: int = Field(..., gt=0)  # mayor a 0
    unit_price: PositiveFloat
    subtotal: PositiveFloat


class SaleCreate(BaseModel):
    branch_id: str
    items: list[SaleItem] = Field(..., min_length=1)  # al menos 1 item
    payment_method: PaymentMethod


class SaleResponse(BaseModel):
    id: str
    branch_id: str
    items: list[SaleItem]
    total: float
    created_at: str
