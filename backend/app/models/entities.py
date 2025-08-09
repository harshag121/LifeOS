from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    energy: str
    duration_min: int
    deadline: Optional[str] = None

class KGNode(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    label: str

class KGEdge(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source: int
    target: int
    relation: str

class AuditLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ts: datetime = Field(default_factory=datetime.utcnow)
    actor: str
    action: str
    meta: str = ""
