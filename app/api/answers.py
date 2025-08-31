from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api.database import get_db

router = APIRouter(prefix="/questions/{question_id}/answers", tags=["answers"])

@router.post("/", response_model=schemas.AnswerRead)
def add_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_answer(db, question_id, answer)
    except ValueError:
        raise HTTPException(status_code=404, detail="Question not found")

@router.get("/{answer_id}", response_model=schemas.AnswerRead)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.delete("/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    crud.delete_answer(db, answer_id)
    return {"detail": "Answer deleted"}