from fastapi import FastAPI, Depends, HTTPException, Header
from firebase_admin import auth
from .database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

# ✅ Middleware: Authenticate Users with Firebase Token
async def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")

    token = authorization.split("Bearer ")[-1]  # Extract token
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# ✅ Protected Route
@app.get("/protected")
async def protected_route(user=Depends(get_current_user)):
    return {"message": "This is a protected route", "user": user}

# ✅ Public Route
@app.get("/")
async def public_route():
    return {"message": "Public endpoint - no auth required"}


# Ensure FastAPI starts correctly in Docker
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
