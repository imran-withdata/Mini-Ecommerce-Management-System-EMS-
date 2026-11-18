from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# 1. Schema for product creation (Request Body) ..........use of post() endpoint
class ProductCreate(BaseModel):
    name : str
    description  : Optional[str]
    price : float = Field(..., gt=0, description="The value must be greater than 0.")
    stock : str = Field( default=0, ge=0, description="Stock must be 0 or greater")
    category_id : int







# 2. Schema for updating a product (all fields are optional) .... Use of put() edpoint
class ProductUpdate(BaseModel):
    name : Optional[str] = None
    description  : Optional[str] = None
    price : Optional[float] = Field( None, gt=0, description="The value must be greater than 0.")
    stock : Optional[int] = Field(None, ge=0, description="Stock must be 0 or greater")
    category_id : Optional[int] = None




# 3. Schema for reading products from the database or displaying a response.... Use of get() edpoint
class ProductResponse(BaseModel):
    id : int
    name : str
    description : str
    price : float = Field(..., gt=0, description="The value must be greater than 0.")
    stock : str = Field( default=0, ge=0, description="Stock must be 0 or greater")
    is_active : bool
    cateory_id : int
    # For converting database objects into a response (required for GET APIs)
    model_config = ConfigDict(from_attributes=True)

