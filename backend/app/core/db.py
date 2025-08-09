from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import os

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "lifeos.db"

DB_URL = os.getenv("DB_URL", f"sqlite:///{DB_PATH}")

engine = create_engine(DB_URL, echo=False, connect_args={"check_same_thread": False} if DB_URL.startswith("sqlite") else {})

_initialized = False

def init_db():
    global _initialized
    if _initialized:
        return
    from backend.app.models.entities import Task, KGNode, KGEdge, AuditLog  # noqa: F401
    SQLModel.metadata.create_all(engine)
    _initialized = True

def get_session() -> Session:
    init_db()
    return Session(engine)

init_db()
