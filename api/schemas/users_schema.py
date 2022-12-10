"""Pydantic schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from pydantic import BaseModel
from api.schemas import items_schema, tasks_schema


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
    items: List[items_schema.Item] = []
    tasks: List[tasks_schema.Task] = []

    class Config:
        """
        Object Relational Mapping Mode.
        """
        orm_mode = True
