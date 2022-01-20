from .crud_base import CRUDBase
from backend.models import Item
from backend.schemas import ItemCreate, ItemUpdate

item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)