"""
SQLAlchemy を使ってデータベース接続とセッション管理を行うための設定する。
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
"""
create_engine：データベースとの接続エンジンを作成
declarative_base：モデル定義に必要なベースクラスを生成
sessionmaker：ORM セッションを生成するファクトリ
"""

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/db.sqlite3")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} 
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    """
    DBセッションを取得し、リクエスト後にクローズするDependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()