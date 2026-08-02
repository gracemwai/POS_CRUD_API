from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from database import Base

class Receipt(Base):
    __tablename__="receipts"

    receipt_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=False, unique=True)
    receipt_number = Column(String, nullable=False, unique=True)
    delivery_method = Column(String, nullable=False)
    issued_at = Column(DateTime(timezone=True), nullable=False)

    sale = relationship("Sale", back_populates="receipt")