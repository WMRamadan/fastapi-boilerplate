"""Task model."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


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
