import datetime as _dt
import pydantic as _pydantic

class _BasePlayer(_pydantic.BaseModel):
    username: str
    inventoryid: int

class Player(_BasePlayer):
    id: int
    model_config = _pydantic.ConfigDict(from_attributes=True)

class CreatePlayer(_BasePlayer):
    pass