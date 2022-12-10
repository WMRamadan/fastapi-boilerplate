"""Database models."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    """
    User model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    """
    Task model.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer, index=False)
    task_id = Column(String, index=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")


class Item(Base):
    """
    Item model.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
