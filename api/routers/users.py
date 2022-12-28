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
from api.schemas import items_schema, tasks_schema, users_schema, status_schema
from .. import database


router = APIRouter()


@router.post("/users/", response_model=users_schema.User)
def create_user(user: users_schema.UserCreate, db_session: Session = Depends(database.get_db)):
    """
    Create user router.
    :param user: The user schema.
    :param db_session: The database session.
    """
    db_user = crud.get_user_by_email(db_session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db_session=db_session, user=user)


@router.get("/users/", response_model=List[users_schema.User])
def read_users(skip: int = 0, limit: int = 100,
db_session: Session = Depends(database.get_db)):
    """
    Get all users router.
    :param skip: The offset used when paging.
    :param limit: The number of users to retrieve per query.
    :param db_session: The database session.
    """
    users = crud.get_users(db_session, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/users/{user_id}", response_model=users_schema.User)
def read_user(user_id: int, db_session: Session = Depends(database.get_db)):
    """
    Get user by User ID router.
    :param user_id: The User ID.
    :param db_session: The database session.
    """
    db_user = crud.get_user(db_session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.patch("/users/{user_id}", response_model=users_schema.User)
def update_user(user_id: int, user: users_schema.UserCreate, db_session: Session = Depends(database.get_db)):
    """
    Update user by User ID router.
    :param user_id: The User ID.
    :param db_session: The database session.
    """
    db_user = crud.update_user(db_session, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=status_schema.Status)
def delete_user(user_id: int, db_session: Session = Depends(database.get_db)):
    """
    Delete user by User ID router.
    :param user_id: The User ID.
    :param db_session: The database session.
    """

    db_user = crud.delete_user(db_session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return status_schema.Status(status=f"Deleted user {user_id}")


@router.post("/users/{user_id}/items/", response_model=items_schema.Item)
def create_item_for_user(user_id: int, item: items_schema.ItemCreate,
db_session: Session = Depends(database.get_db)):
    """
    Create the user item router.
    :param user_id: The ID of the user.
    :param item: The item schema.
    :param db_session: The database session.
    """
    return crud.create_user_item(db_session=db_session, item=item, user_id=user_id)

@router.delete("/users/{user_id}/items/{item_id}", response_model=status_schema.Status)
def delete_item_for_user(user_id: int, item_id: int,
db_session: Session = Depends(database.get_db)):
    """
    Delete the user item router.
    :param user_id: The ID of the user.
    :param item_id: The ID of the item.
    :param db_session: The database session.
    """
    db_item = crud.delete_user_item(db_session=db_session, item_id=item_id, user_id=user_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return status_schema.Status(status=f"Deleted Item {item_id} for user {user_id}")

@router.post("/users/{user_id}/tasks/", response_model=tasks_schema.Task)
def create_task_for_user(user_id: int, task: tasks_schema.TaskCreate,
db_session: Session = Depends(database.get_db)):
    """
    Create the user task router.
    :param user_id: The ID of the user.
    :param task: The task schema.
    :param db_session: The database session.
    """
    return crud.create_user_task(db_session=db_session, task=task, user_id=user_id)
