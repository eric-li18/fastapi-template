from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Body, Query
from sqlalchemy.orm import Session
from backend import crud, schemas
from .util import get_db

router = APIRouter()


@router.get("/{item_id}/", response_model=schemas.Item)
def get_item(
    db: Session = Depends(get_db),
    item_id: int = Path(..., title="ID of item to get", ge=1),
):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(
            status_code=404, detail=f"Item with id: {item_id} not found."
        )
    return item


@router.get("/", response_model=List[schemas.Item])
def get_items(
    db: Session = Depends(get_db),
    limit: int = Query(None, title="Upper limit of records returned", ge=1),
):
    items = crud.item.get_multi(db, limit)
    if not items:
        raise HTTPException(status_code=404, detail=f"Database is empty.")
    return items


@router.post("/", response_model=schemas.Item)
def create_item(
    db: Session = Depends(get_db),
    item: schemas.ItemCreate = Body(..., title="Item to be created."),
):
    created_item = crud.item.create(db, item)
    return created_item


@router.delete("/{item_id}/", response_model=schemas.Item)
def remove_item(
    db: Session = Depends(get_db),
    item_id: int = Path(..., title="ID of item to delete."),
):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(
            status_code=404, detail=f"Item with id: {item_id} not found."
        )
    crud.item.remove(db, item_id)
    return item


@router.patch("/", response_model=schemas.ItemUpdate)
def update_item(
    db: Session = Depends(get_db),
    item: schemas.ItemUpdate = Body(..., title="Item fields to update."),
):
    updated_item = crud.item.update(db, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail=f"Item not found.")
    return updated_item
