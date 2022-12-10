"""This module is for the tasks router."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.helpers import crud
from .. import schemas, database


router = APIRouter()


@router.get("/tasks/", response_model=List[schemas.Task])
async def read_tasks(skip: int = 0, limit: int = 100,
db_session: Session = Depends(database.get_db)):
    """
    Get all tasks router.
    :param skip: The offset used when paging.
    :param limit: The number of items to retrieve per query.
    :param db: The database session.
    """
    tasks = crud.get_tasks(db_session, skip=skip, limit=limit)
    return tasks

@router.get("/tasks/{task_id}")
async def read_task(task_id: str):
    """
    Get task by User ID router.
    :param task_id: The Task ID.
    """
    task_result = crud.get_task(task_id=task_id)
    return task_result
