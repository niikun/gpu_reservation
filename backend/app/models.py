from sqlalchemy import Column, Integer,String, DateTime, ForeignKey, Enum, Float
from sqkalchemy.orm import relationship
from .database import Base
import enum

class Role(enum.Enum):
    user = "user"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(Role), default=Role.user)

class Server(Base) :
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    gpu_type=Column(String)
    status = Column(String, default="available")

