from sqlalchemy import(
    Column, 
    Integer,
    String
) 
from sqlalchemy.orm import relationship
from database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=False)

    payments = relationship("Payment", back_populates="supplier")