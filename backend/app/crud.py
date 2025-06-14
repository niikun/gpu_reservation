from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    # ユーザー一覧取得
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Server CRUD
def get_server(db: Session, server_id: int):
    return db.query(models.Server).filter(models.Server.id == server_id).first()

def get_servers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Server).offset(skip).limit(limit).all()

def create_server(db: Session, server: schemas.ServerCreate):
    db_server = models.Server(name=server.name, gpu_type=server.gpu_type)
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

# Reservation CRUD
def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()

def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reservation).offset(skip).limit(limit).all()

def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    # インスタンス化時のキーワード引数問題を回避して属性を設定
    db_res = models.Reservation()
    db_res.user_id = reservation.user_id
    db_res.server_id = reservation.server_id
    db_res.start_dt = reservation.start_dt
    db_res.end_dt = reservation.end_dt
    db_res.status = "pending"
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res

def cancel_reservation(db: Session, reservation_id: int):
    res = get_reservation(db, reservation_id)
    if not res:
        return None
    res.status = "cancelled"
    db.commit()
    db.refresh(res)
    return res

def update_reservation_status(db: Session, reservation_id: int, status: str):
    res = get_reservation(db, reservation_id)
    if not res:
        return None
    res.status = status
    db.commit()
    db.refresh(res)
    return res