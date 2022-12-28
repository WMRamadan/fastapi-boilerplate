"""Pydantic Question schemas."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class PydanticObjectId(ObjectId):
    """
    MongoDB ObjectId.
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string", example="63ac23ab8c79ddb40f9cad2f")


class QuestionBase(BaseModel):
    """
    Question Base Schema.
    """
    id: PydanticObjectId = Field(None, alias="_id")
    question: str
    answer: str

    class Config:
        """
        Object Relational Mapping Mode.
        """
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class QuestionResponse(BaseModel):
    """
    Question Response Schema.
    """
    status: str
    question: QuestionBase


class ListQuestionResponse(BaseModel):
    """
    Question Response List Schema.
    """
    status: str
    results: int
    questions: List[QuestionBase]
