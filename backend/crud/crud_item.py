from ..db.session import Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import Generic, TypeVar, Type, Optional, List, Any


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """Generic CRUD operations for ModelType"""
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, id: Any) -> List[ModelType]:
        return db.query(self.model).filter(self.model.id == id).all()

    def create(self, db: Session, schema: CreateSchemaType) -> ModelType:
        data = jsonable_encoder(schema)
        obj = self.model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(
        self, db: Session, obj: ModelType, schema: UpdateSchemaType
    ) -> ModelType:
        data = jsonable_encoder(schema)
        update_data = schema.dict(exclude_unset=True)

        for field in data:
            if field in update_data:
                setattr(obj, field, update_data[field])

        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def remove(self, db: Session, id: int):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj