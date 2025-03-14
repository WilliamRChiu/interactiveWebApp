import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import relationship
from ..database import database as _database


class Contact(_database.Base):
    __tablename__ = "contacts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, primary_key = False, index = True)
    last_name = _sql.Column(_sql.String, index = True)
    email = _sql.Column(_sql.String, index = True, unique = True)
    phone_number = _sql.Column(_sql.String, index = True, unique=True)
    date_created = _sql.Column(_sql.DateTime, default = _dt.datetime.now)

class Object(_database.Base):
    __tablename__ = "objects"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    object_name = _sql.Column(_sql.String, index = True)
    object_description = _sql.Column(_sql.String, index = True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
    date_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
    object_status = _sql.Column(_sql.Boolean, index=True)

class Player(_database.Base):
    __tablename__ = "players"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    username = _sql.Column(_sql.String, index = True)
    inventoryid = _sql.Column(_sql.Integer, unique = True)

class Items(_database.Base):
    __tablename__ = "items"
    id = _sql.Column(_sql.Integer, primary_key = True, index = True)
    name = _sql.Column(_sql.String, nullable = False)
    description = _sql.Column(_sql.String, nullable = True)
    rarity = _sql.Column(_sql.String, nullable = False)



class Inventory(_database.Base):
    __tablename__ = "inventory"
    id = _sql.Column(_sql.Integer, primary_key = True, index = True)
    player_id = _sql.Column(_sql.Integer, _sql.ForeignKey("players.id"))
    item_id = _sql.Column(_sql.Integer, _sql.ForeignKey("items.id"))
    quantity = _sql.Column(_sql.Integer, default = 1)
    player = relationship("Player", back_populates="inventory")
    item = relationship("Items")
    
