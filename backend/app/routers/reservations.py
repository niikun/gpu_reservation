from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ReservationRead)
async def create_reservation(res_in: schemas.ReservationCreate, db: Session = Depends(get_db)):
    if not crud.get_user(db, res_in.user_id):
        raise HTTPException(404, "User not found")
    if not crud.get_server(db, res_in.server_id):
        raise HTTPException(404, "Server not found")
    db_res = crud.create_reservation(db, res_in)
    res_dict = {
        'id': db_res.id,
        'user_id': db_res.user_id,
        'server_id': db_res.server_id,
        'start_dt': db_res.start_dt,
        'end_dt': db_res.end_dt,
        'status': db_res.status,
        'priority_score': db_res.priority_score
    }
    return schemas.ReservationRead(**res_dict)

@router.get("/", response_model=list[schemas.ReservationRead])
async def list_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    res_list = crud.get_reservations(db, skip, limit)
    result = []
    for r in res_list:
        result.append(schemas.ReservationRead(**{
            'id': r.id,
            'user_id': r.user_id,
            'server_id': r.server_id,
            'start_dt': r.start_dt,
            'end_dt': r.end_dt,
            'status': r.status,
            'priority_score': r.priority_score
        }))
    return result

@router.post("/{reservation_id}/cancel", response_model=schemas.ReservationRead)
async def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    res = crud.cancel_reservation(db, reservation_id)
    if not res:
        raise HTTPException(404, "Reservation not found")
    return schemas.ReservationRead(**{
        'id': res.id,
        'user_id': res.user_id,
        'server_id': res.server_id,
        'start_dt': res.start_dt,
        'end_dt': res.end_dt,
        'status': res.status,
        'priority_score': res.priority_score
    })