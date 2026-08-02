from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    sale_id: int
    supplier_id: int
    payment_method: str
    amount_paid: Decimal
    change_given: Decimal
    transaction_reference: Optional[str] = None
    paid_at: datetime


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    sale_id: Optional[int] = None
    supplier_id: Optional[int] = None
    payment_method: Optional[str] = None
    amount_paid: Optional[Decimal] = None
    change_given: Optional[Decimal] = None
    transaction_reference: Optional[str] = None
    paid_at: Optional[datetime] = None


class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    payment_id: int