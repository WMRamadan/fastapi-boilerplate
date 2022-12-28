"""This module is for the questions router."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from api.helpers import crud
from api.schemas import questions_schema

router = APIRouter()

@router.get("/questions/", response_model=questions_schema.ListQuestionResponse)
def read_questions(skip: int = 0, limit: int = 10):
    """
    Get all questions router.
    :param skip: The offset used when paging.
    :param limit: The number of items to retrieve per query.
    :param mongo_db: The database client.
    """
    questions = crud.get_questions(skip=skip, limit=limit)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return {'status': 'success', 'results': len(questions), 'questions': questions}

@router.post("/questions/", response_model=questions_schema.QuestionResponse)
def create_question(question: questions_schema.QuestionBase):
    """
    Post questions router.
    :param question: The question schema.
    """
    res = crud.create_question(question=question)
    return {"status": "success", "question": res}