from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Boolean
)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    pin_code = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    sales = relationship("Sale", back_populates="user")