"""This module is for the users router."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api.helpers import crud
from .. import schemas, database

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db_session: Session = Depends(database.get_db)):
    """
    Create user router.
    :param user: The user schema.
    :param db_session: The database session.
    """
    db_user = crud.get_user_by_email(db_session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db_session=db_session, user=user)


@router.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100,
db_session: Session = Depends(database.get_db)):
    """
    Get all users router.
    :param skip: The offset used when paging.
    :param limit: The number of users to retrieve per query.
    :param db_session: The database session.
    """
    users = crud.get_users(db_session, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db_session: Session = Depends(database.get_db)):
    """
    Get user by User ID router.
    :param user_id: The User ID.
    :param db_session: The database session.
    """
    db_user = crud.get_user(db_session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
async def create_item_for_user(user_id: int, item: schemas.ItemCreate,
db_session: Session = Depends(database.get_db)):
    """
    Create the user item router.
    :param user_id: The ID of the user.
    :param item: The item schema.
    :param db_session: The database session.
    """
    return crud.create_user_item(db_session=db_session, item=item, user_id=user_id)
