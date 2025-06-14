from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ServerRead)
async def create_server(server: schemas.ServerCreate, db: Session = Depends(get_db)):
    existing = crud.get_servers(db, skip=0, limit=1)
    if any(s.name == server.name for s in existing):
        raise HTTPException(status_code=400, detail="Server already exists")
    return crud.create_server(db, server)

@router.get("/", response_model=list[schemas.ServerRead])
async def list_servers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_servers(db, skip, limit)