"""Pydantic schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from pydantic import BaseModel


class TaskBase(BaseModel):
    """
    Task Base Schema.
    """
    time: int


class TaskCreate(TaskBase):
    """
    Task Create Schema.
    """
    pass


class Task(TaskBase):
    """
    Task Schema.
    """
    id: int
    task_id: str
    owner_id: int

    class Config:
        """
        Object Relational Mapping Mode.
        """
        orm_mode = True


class ItemBase(BaseModel):
    """
    Item Base Schema.
    """
    title: str
    description: str


class ItemCreate(ItemBase):
    """
    Item Create Schema.
    """
    pass


class Item(ItemBase):
    """
    Item Schema.
    """
    id: int
    owner_id: int

    class Config:
        """
        Object Relational Mapping Mode.
        """
        orm_mode = True


class UserBase(BaseModel):
    """
    User Base Schema.
    """
    email: str


class UserCreate(UserBase):
    """
    User Create Schema.
    """
    password: str


class User(UserBase):
    """
    User Schema.
    """
    id: int
    is_active: bool
    items: List[Item] = []
    tasks: List[Task] = []

    class Config:
        """
        Object Relational Mapping Mode.
        """
        orm_mode = True
