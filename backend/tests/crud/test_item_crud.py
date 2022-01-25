from sqlalchemy.orm import Session
from backend.crud import item
from backend.schemas import ItemCreate, ItemUpdate
from backend.tests.utils import utils


def test_create_item(db: Session):
    itemname = utils.random_string()
    price = utils.random_float()
    item_model = ItemCreate(itemname=itemname, price=price)
    created_item = item.create(db, item_model)
    assert created_item.itemname == itemname
    assert created_item.price == price
