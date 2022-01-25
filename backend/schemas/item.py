from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: Optional[int]
    itemname: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    description: Optional[str]


# Properties to receive on item creation
class ItemCreate(ItemBase):
    itemname: str
    price: float


# Properties to receive on item update
class ItemUpdate(ItemBase):
    id: int


# Properties to return to client
class Item(ItemBase):
    id: int
    itemname: str
    price: float

    # Tells the Pydantic model to read data in dict and ORM model:
    #
    # We can access id by:
    # id = data.id
    #     or
    # id = data["id"]
    class Config:
        orm_mode = True
