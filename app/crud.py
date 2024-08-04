from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def create_test_question(db: Session, question: schemas.QuestionCreate, test_id: int):
    db_question = models.Question(**question.dict(), test_id=test_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def submit_test(db: Session, test_id: int, user_id: int, answers: List[schemas.AnswerSubmit]):
    test = db.query(models.Test).filter(models.Test.id == test_id).first()
    if not test:
        raise ValueError("Test not found")

    score = 0
    for answer in answers:
        question = db.query(models.Question).filter(models.Question.id == answer.question_id, models.Question.test_id == test_id).first()
        if question and question.correct_answer == answer.answer:
            score += 1

    test_result = models.TestResult(user_id=user_id, test_id=test_id, score=score)
    db.add(test_result)
    db.commit()
    db.refresh(test_result)
    return test_result

def get_all_results(db: Session):
    return db.query(models.TestResult).all()

def get_user_results(db: Session, user_id: int):
    return db.query(models.TestResult).filter(models.TestResult.user_id == user_id).all()