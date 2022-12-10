"""Pydantic Task schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
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
