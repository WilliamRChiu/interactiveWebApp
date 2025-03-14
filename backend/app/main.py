import fastapi as _fastapi
from firebase_admin import auth

from sqlalchemy.orm import Session

import app.database.database as _database

import app.services.services as _services
import app.Schemas.contactsSchema as _contactSchemas
import app.Schemas.playerSchema as _playerSchemas
import app.models.models as _models



app = _fastapi.FastAPI()

@app.post("/api/contacts/", response_model=_contactSchemas.Contact)
async def create_contact(contact: _contactSchemas.CreateContact, db: Session=_fastapi.Depends(_database.get_db)):
    return await _services.create_contact(contact=contact, db = db)

@app.on_event("startup")
async def startup():
    _services._add_tables()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# This will create the tables for all models inherited from Base
# _database.Base.metadata.create_all(bind=engine)