from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str
    delivery_method: str
    issued_at: datetime


class ReceiptCreate(ReceiptBase):
    pass


class ReceiptUpdate(BaseModel):
    sale_id: Optional[int] = None
    receipt_number: Optional[str] = None
    delivery_method: Optional[str] = None
    issued_at: Optional[datetime] = None


class ReceiptRead(ReceiptBase):
    model_config = ConfigDict(from_attributes=True)

    receipt_id: int