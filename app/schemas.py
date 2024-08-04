from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    title: str
    description: str

class TestCreate(TestBase):
    pass

class Test(TestBase):
    id: int
    questions: List["Question"] = []

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    question_text: str
    correct_answer: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    test_id: int

    class Config:
        orm_mode = True

class AnswerSubmit(BaseModel):
    question_id: int
    answer: str

class TestResult(BaseModel):
    id: int
    user_id: int
    test_id: int
    score: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None