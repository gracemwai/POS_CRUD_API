from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    barcode: str
    name: str
    category_id: int
    price: Decimal


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    barcode: Optional[str] = None
    name: Optional[str] = None
    category_id: Optional[int] = None
    price: Optional[Decimal] = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    product_id: int