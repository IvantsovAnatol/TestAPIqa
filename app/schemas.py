from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class AnswerBase(BaseModel):
    user_id: str
    text: str = Field(..., min_length=1)

class AnswerCreate(AnswerBase):
    pass

class AnswerRead(AnswerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class QuestionBase(BaseModel):
    text: str = Field(..., min_length=1)

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    created_at: datetime
    answers: List[AnswerRead] = []

    class Config:
        from_attributes = True