from ..database import database as _database
from ..models import models as _models
import app.Schemas.playerSchema as _playerSchema
import app.Schemas.contactsSchema as _contactSchema
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

async def create_contact(contact: _contactSchema.CreateContact, db: "Session") -> _contactSchema.Contact:
    db_contact = _models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return _contactSchema.Contact.model_validate(db_contact)



async def create_player(player: _playerSchema.CreatePlayer, db : "Session") -> _playerSchema.Player:
    db_player = _models.Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return _playerSchema.Player.model_validate(db_player)