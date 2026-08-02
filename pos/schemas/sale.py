from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    customer_id: Optional[int] = None
    user_id: int
    subtotal: Decimal
    tax_amount: Decimal
    discount_amount: Decimal = 0
    grand_total: Decimal
    status: str


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    customer_id: Optional[int] = None
    user_id: Optional[int] = None
    subtotal: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    discount_amount: Optional[Decimal] = None
    grand_total: Optional[Decimal] = None
    status: Optional[str] = None


class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    sale_id: int
    created_at: datetime
    updated_at: datetime