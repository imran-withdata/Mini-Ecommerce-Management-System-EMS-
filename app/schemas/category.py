from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr


# ................Create Catagory.............Add a new catagory...........use of post() endpoint 
class CategoryCreate(BaseModel):
    name : str
    description : Optional[str] = None


# ....................Catagory Update.............. To change or Update the previous category......Use of put() endpoint
class CategoryUpdate(BaseModel):
    name : Optional[str] = None
    description : Optional[str] = None



# ...............Category Response.........Show data........ use of get() endpint
class CategoryResponse(BaseModel):
    id : int
    name : str
    description : Optional[str] = None
    model_config = ConfigDict(from_attributes=True) # Output / Response Schema need this code


