import fastapi as _fastapi
from firebase_admin import auth

from sqlalchemy.orm import Session

import app.database.database as _database

import app.services.services as _services
import app.Schemas.contactsSchema as _contactSchemas
import app.models.models as _models



app = _fastapi.FastAPI()

@app.post("/api/contacts/", response_model=_contactSchemas.Contact)
async def create_contact(contact: _contactSchemas.CreateContact, db: Session=_fastapi.Depends(_database.get_db)):
    return await _services.create_contact(contact=contact, db = db)
    # new_contact = _models.Contact(
    #     first_name = contact.first_name,
    #     last_name = contact.last_name,
    #     email = contact.email,
    #     phone_number = contact.phone_number
    # )  


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
