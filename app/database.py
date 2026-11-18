# database.py এর কাজ একটাই: Python কোডকে MySQL এর সঙ্গে সংযুক্ত করা।

import os # Python এর নিজস্ব। কম্পিউটারের environment variable (যেমন .env এর তথ্য) পড়তে সাহায্য করে
from dotenv import load_dotenv # .env ফাইলটি পড়ে। এতে MySQL এর পাসওয়ার্ড লুকিয়ে রাখা হয়
from sqlalchemy import create_engine # MySQL শুধু SQL ভাষা বোঝে। আমরা লিখছি Python। SQLAlchemy তোমার Python কোডকে SQL এ অনুবাদ করে MySQL কে দেয়, আর MySQL এর উত্তর আবার Python এ ফিরিয়ে আনে।
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()