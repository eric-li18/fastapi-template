from typing import Generator
from backend.db.base import Base
from backend.db.session import engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)