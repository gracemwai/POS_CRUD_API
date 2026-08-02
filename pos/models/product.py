from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Numeric
)
from sqlalchemy.orm import relationship
from database import Base


class Product(Base):
    __tablename__="products"

    product_id=Column(Integer, primary_key=True, index=True)
    barcode=Column(String,nullable=False)
    name=Column(String,nullable=False)
    category_id=Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    price=Column(Numeric(10,2),nullable=False)

    category=relationship("Category",back_populates="products")





