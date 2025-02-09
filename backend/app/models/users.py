from sqlalchemy import Column, Integer, String
from ..database import metadata, engine

class User(metadata):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)

metadata.create_all(engine)
