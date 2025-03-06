import datetime as _dt
import sqlalchemy as _sql
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
    __tablename__ = "Player"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    username = _sql.Column(_sql.String, index = True)
    InventoryID = _sql.Column(_sql.Integer, unique = True)
