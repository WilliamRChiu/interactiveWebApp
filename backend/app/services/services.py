from ..database import database as _database
from ..models import models as _models

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)