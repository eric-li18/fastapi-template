from ast import In
from email.policy import default
from ..db.session import Base
from sqlalchemy import Column, String, Integer, Float


class Item(Base):
    __table__name = "items"

    id = Column(Integer, primary_key=True, index=True)
    itemname = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    description = Column(String)