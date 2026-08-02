from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship
from database import Base, TimestampMixin

class Customer(Base, TimestampMixin):
    __tablename__="customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    loyalty_points = Column(Integer, nullable=False, default=0)

    sales = relationship("Sale", back_populates="customer")