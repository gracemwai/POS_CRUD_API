from sqlalchemy import(
    Column, 
    Integer, 
    String,
    Numeric, 
    ForeignKey
)
from sqlalchemy.orm import relationship
from database import Base, TimestampMixin

class Sale(Base, TimestampMixin):
    __tablename__="sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)
    tax_amount = Column(Numeric(10, 2), nullable=False)
    discount_amount = Column(Numeric(10, 2), nullable=False, default=0)
    grand_total = Column(Numeric(10, 2), nullable=False)
    status = Column(String, nullable=False)


    customer = relationship("Customer", back_populates="sales")
    user = relationship("User",back_populates="sales")
    sale_items = relationship("SaleItem", back_populates="sale")
    payments = relationship("Payment", back_populates="sale")
    receipt = relationship("Receipt", back_populates="sale", uselist=False)