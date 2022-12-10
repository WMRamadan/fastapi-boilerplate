"""This module is for the items router."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.helpers import crud
from .. import schemas, database


router = APIRouter()


@router.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100,
db_session: Session = Depends(database.get_db)):
    """
    Get all items router.
    :param skip: The offset used when paging.
    :param limit: The number of items to retrieve per query.
    :param db: The database session.
    """
    items = crud.get_items(db_session, skip=skip, limit=limit)
    return items
