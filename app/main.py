from fastapi import FastAPI

app = FastAPI(title= "E-commerce Order Management")

@app.get("/")
def Default():
    return{"message" : "Ecommerce Order Management System is running"}






from app.database import Base
from app import models # Import models Package 



from app.database import engine
from app.models import Base  # সব মডেল যেন __init__.py এর মাধ্যমে লোড হয়

# অ্যাপ রান হওয়ার সময় ডেটাবেজে টেবিল তৈরি করবে
Base.metadata.create_all(bind=engine)




# রাউটারটি অ্যাপ্লিকেশনে যুক্ত করুন
from app.routers.category import router as category_router
app.include_router(category_router)

