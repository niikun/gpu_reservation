from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class Role(str, Enum):
    user = "user"
    admin = "admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: Role

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Role
    class Config:
        orm_mode = True

class ServerCreate(BaseModel):
    name:str
    gpu_type: str

class ServerRead(BaseModel):
    id: int
    name: str
    gpu_type: str
    status:str
    class Config:
        orm_mode = True

class ReservationCreate(BaseModel):
    user_id: int
    server_id:int
    start_dt : datetime
    end_dt: datetime

class ReservationRead(BaseModel):
    id: int
    user_id:int
    server_id:int
    start_dt: datetime
    end_dt: datetime
    status: str
    priority_score: float | None
    class Config:
        orm_mode = True

