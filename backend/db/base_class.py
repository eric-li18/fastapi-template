from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# Both base_class.py and base.py are needed to overcome shadowing imports
# See:
# https://stackoverflow.com/a/54119660


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()