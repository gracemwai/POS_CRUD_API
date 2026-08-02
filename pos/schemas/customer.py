from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    loyalty_points: int = 0


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    loyalty_points: Optional[int] = None


class CustomerRead(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    customer_id: int
    created_at: datetime
    updated_at: datetime