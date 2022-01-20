from backend.db.base import Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import Generic, TypeVar, Type, Optional, List, Any


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """Generic CRUD operations for ModelType"""
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Return a single row from database session db where row id matches id.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, limit: int = 100) -> List[ModelType]:
        """
        Return list of rows from database session db up to a limit.
        """
        return db.query(self.model).limit(limit).all()

    def create(self, db: Session, create_obj: CreateSchemaType) -> ModelType:
        """
        Creates record in database following schema, and returns created
        object following ModelType.
        """
        create_data = jsonable_encoder(create_obj)
        new_model = self.model(**create_data)
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
        return new_model

    def update(self, db: Session, update_obj: UpdateSchemaType) -> ModelType:
        """
        Updates record in database following schema, and returns updated
        object following ModelType.
        """
        data_to_update = jsonable_encoder(update_obj)
        update_data = CreateSchemaType.dict(exclude_unset=True)

        for field in data_to_update:
            if field in update_data:
                setattr(update_obj, field, update_data[field])

        db.add(update_obj)
        db.commit()
        db.refresh(update_obj)
        return update_obj

    def remove(self, db: Session, id: int) -> None:
        """
        Removes record from database where record id matches id.
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj