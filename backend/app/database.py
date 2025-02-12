from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials

file_path = os.path.join(os.path.dirname(__file__), "firebase_service_account.json")
cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()