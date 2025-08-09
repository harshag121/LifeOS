from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Literal
from sqlmodel import select
from backend.app.core.db import get_session
from backend.app.models.entities import Task, AuditLog

router = APIRouter()

Energy = Literal["mental", "physical", "creative"]

class TaskIn(BaseModel):
    title: str
    energy: Energy
    duration_min: int
    deadline: str | None = None
    depends_on: list[int] = []

@router.post("/create")
async def create(task: TaskIn, session=Depends(get_session)):
    db_task = Task(title=task.title, energy=task.energy, duration_min=task.duration_min, deadline=task.deadline)
    session.add(db_task)
    session.add(AuditLog(actor="system", action="task.create", meta=db_task.title))
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/list")
async def list_tasks(session=Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks

@router.get("/prioritize")
async def prioritize(session=Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    def sort_key(t: Task):
        return (t.deadline or "9999-12-31", t.duration_min)
    ordered = sorted(tasks, key=sort_key)
    return ordered
