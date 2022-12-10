"""This module is the helper for all crud operations."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from sqlalchemy.orm import Session
from .. import models, schemas


def get_user(db_session: Session, user_id: int):
    """
    Get user by User ID helper.
    :param db_session: The database session.
    :param user_id: The User ID.
    """
    return db_session.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db_session: Session, email: str):
    """
    Get user by User email helper.
    :param db_session: The database session.
    :param email: The User Email.
    """
    return db_session.query(models.User).filter(models.User.email == email).first()


def get_users(db_session: Session, skip: int = 0, limit: int = 100):
    """
    Get all users helper.
    :param db_session: The database session.
    :param skip: The offset used when paging.
    :param limit: The number of users to retrieve per query.
    """
    return db_session.query(models.User).offset(skip).limit(limit).all()


def create_user(db_session: Session, user: schemas.UserCreate):
    """
    Create user helper.
    :param db_session: The database session.
    :param user: The user schema.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
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
    return db_session.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db_session: Session, item: schemas.ItemCreate, user_id: int):
    """
    Create the user item helper.
    :param db_session: The database session.
    :param item: The item schema.
    :param limit: The User ID to add the item to.
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)
    return db_item
