# from datetime import datetime, timedelta
from sqlalchemy import Boolean, Column, Float, Integer, String, Numeric, ForeignKey
from app.database import Base



class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), unique=True, nullable=False, index=True) # nullable=False Means name is not Optional .Its must be useed 
    description = Column(String(100), nullable= True) # nullable= True means Description is optional
    price = Column(Numeric(10,2),nullable=False)
    stock = Column(Integer, default=0, nullable=False) # default=0 Means If no value is provided, it will default to 0.
    is_active =Column(Boolean, default=True, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), nullable=False)




# Relationship between product and category (Many-to-One)
from sqlalchemy.orm import relationship
category = relationship("Category", back_populates="products")


