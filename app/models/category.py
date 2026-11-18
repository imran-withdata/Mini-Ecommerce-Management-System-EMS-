# from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base



# Category : id (primary key), name (unique, not null), description (optional)
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index= True)
    description = Column(String(100), nullable=True )






# Relationship between categories and products (One-to-Many)
from sqlalchemy.orm import relationship
products = relationship(
    "product", back_populates="category", cascade="all, delete-orphan"
    )

