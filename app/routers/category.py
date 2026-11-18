from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db



# models<category import
from app.models.category import Category

# schemas<category import
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate




router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


#.......................Create  a new Category / Use post() Request

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
# Function for creating a new category
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
  # Check whether a category with the same name already exists in the database
  existing_category = (
      db.query(Category).filter(Category.name == category.name).first()
  )
  if existing_category:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Category with this name already exists",
    )

  new_category = Category(
      name=category.name, description=category.description
  )
  db.add(new_category)
  db.commit()
  db.refresh(new_category)
  return new_category






# .................Show all category use get end point............
@router.get("/" , response_model= list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
  categories = db.query(Category).all()
  return categories





# ..........................Show Specefic Category.................
@router.get("/{category_id}", response_model= CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db) ):
  category = db.query(Category).filter(Category.id == category_id).first()
  if not category:
    raise HTTPException (status_code=404, detail="Category not found")
  return category

  


# ................Update Catrgory...................
@router.put("/{category_id}", response_model= CategoryResponse)
def UpdateCatrgory(category_id: int, category_update: CategoryUpdate, db: Session = Depends(get_db)):
  category = db.query(Category).filter(Category.id == category_id).first()
  if not category:
    raise HTTPException (status_code=404, detail="Category not found")
  
  # Update only the fields that have been sent
  update_data = category_update.model_dump(exclude_unset=True) # Converting update data into a dictionary
  # Updating data directly
  for key, value in update_data.items():
      setattr(category, key, value)

  db.commit()
  db.refresh(category)
  return category




# .............. Category Delete Use of Delete Request.............
@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def DeleteCategory(category_id: int, db: Session = Depends(get_db)):
  category = db.query(Category).filter(Category.id == category_id).first()
  if not category:
    raise HTTPException(status_code= 404, detail="Category not found")

  db.delete(category)
  db.commit()
  return None






