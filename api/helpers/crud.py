"""This module is the helper for all crud operations."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from celery.result import AsyncResult
from sqlalchemy.orm import Session
from .. import worker
from api.models import user_model, item_model, task_model
from api.schemas import items_schema, tasks_schema, users_schema


def get_user(db_session: Session, user_id: int):
    """
    Get user by User ID helper.
    :param db_session: The database session.
    :param user_id: The User ID.
    """
    return db_session.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_email(db_session: Session, email: str):
    """
    Get user by User email helper.
    :param db_session: The database session.
    :param email: The User Email.
    """
    return db_session.query(user_model.User).filter(user_model.User.email == email).first()


def get_users(db_session: Session, skip: int = 0, limit: int = 100):
    """
    Get all users helper.
    :param db_session: The database session.
    :param skip: The offset used when paging.
    :param limit: The number of users to retrieve per query.
    """
    return db_session.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db_session: Session, user: users_schema.UserCreate):
    """
    Create user helper.
    :param db_session: The database session.
    :param user: The user schema.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_model.User(email=user.email, hashed_password=fake_hashed_password)
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user


def get_items(db_session: Session, skip: int = 0, limit: int = 100):
    """
    Get all items helper.
    :param db_session: The database session.
    :param skip: The offset used when paging.
    :param limit: The number of items to retrieve per query.
    """
    return db_session.query(item_model.Item).offset(skip).limit(limit).all()


def create_user_item(db_session: Session, item: items_schema.ItemCreate, user_id: int):
    """
    Create the user item helper.
    :param db_session: The database session.
    :param item: The item schema.
    :param user_id: The User ID to add the item to.
    """
    db_item = item_model.Item(**item.dict(), owner_id=user_id)
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)
    return db_item


def create_user_task(db_session: Session, task: tasks_schema.TaskCreate, user_id: int):
    """
    Create the user task helper.
    :param db_session: The database session.
    :param task: The task schema.
    :param user_id: The User ID to add the item to.
    """
    task_run = worker.run_task.delay(task.time)
    print(task_run)
    db_task = task_model.Task(**task.dict(), task_id=task_run.id, owner_id=user_id)
    db_session.add(db_task)
    db_session.commit()
    db_session.refresh(db_task)
    print(type(db_task))
    return db_task

def get_tasks(db_session: Session, skip: int = 0, limit: int = 100):
    """
    Get all tasks helper.
    :param db_session: The database session.
    :param skip: The offset used when paging.
    :param limit: The number of tasks to retrieve per query.
    """
    return db_session.query(task_model.Task).offset(skip).limit(limit).all()

def get_task(task_id: int):
    """
    Get task by ID helper.
    :param task_id: The of the task.
    """
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
