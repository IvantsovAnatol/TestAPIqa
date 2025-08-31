from sqlalchemy.orm import Session
from app import models
from app import schemas

def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def get_questions(db: Session):
    return db.query(models.Question).all()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    question = get_question(db, question_id)
    if question:
        db.delete(question)
        db.commit()

def create_answer(db: Session, question_id: int, answer: schemas.AnswerCreate):
    # Проверка существования вопроса
    question = get_question(db, question_id)
    if not question:
        raise ValueError("Question not found")
    db_answer = models.Answer(
        question_id=question_id,
        user_id=answer.user_id,
        text=answer.text
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

def delete_answer(db: Session, answer_id: int):
    answer = get_answer(db, answer_id)
    if answer:
        db.delete(answer)
        db.commit()