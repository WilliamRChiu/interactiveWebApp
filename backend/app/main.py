from fastapi import FastAPI
from firebase_admin import auth

from sqlalchemy.orm import Session




app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
