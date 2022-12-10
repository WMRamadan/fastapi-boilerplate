"""Pydantic Item schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from pydantic import BaseModel


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
