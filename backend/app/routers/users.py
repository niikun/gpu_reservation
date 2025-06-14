from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.UserRead)
async def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user_in)

@router.get("/", response_model=list[schemas.UserRead])
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)