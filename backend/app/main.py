from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from . import models
from .routers import servers, reservations, auth, users

# DB初期化
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Server Reservation API",
    version="0.1.0"
)

# ヘルスチェックエンドポイント
@app.get("/health")
async def health():
    return {"status": "ok"}

# ルーター登録

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(servers.router, prefix="/servers", tags=["servers"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(reservations.router, prefix="/reservations", tags=["reservations"])
