from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)
    payment_method = Column(String, nullable=False)
    amount_paid = Column(Numeric(10, 2), nullable=False)
    change_given = Column(Numeric(10, 2), nullable=False)
    transaction_reference = Column(String, nullable=True)
    paid_at = Column(DateTime(timezone=True), nullable=False)

    sale = relationship("Sale", back_populates="payments")
    supplier = relationship("Supplier", back_populates="payments")