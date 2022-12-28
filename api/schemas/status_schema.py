"""Pydantic Stauts schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from pydantic import BaseModel


class Status(BaseModel):
    status: str
