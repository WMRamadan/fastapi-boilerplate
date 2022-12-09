from .. import crud, schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database

router = APIRouter()


@router.get("/items/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
