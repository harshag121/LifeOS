from datetime import datetime, timedelta
from typing import List, Literal
from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from backend.app.core.db import get_session
from backend.app.models.entities import Task

router = APIRouter()

Algo = Literal["time_blocking", "pomodoro", "flow_state"]

class Block(dict):
    pass

@router.get("/suggest")
async def suggest(
    algorithm: Algo = Query("time_blocking"),
    start: str | None = None,
    session=Depends(get_session),
):
    tasks: List[Task] = session.exec(select(Task)).all()
    tasks = sorted(tasks, key=lambda t: (t.deadline or "9999-12-31", t.duration_min))
    now = datetime.fromisoformat(start) if start else datetime.now().replace(microsecond=0)
    blocks: List[Block] = []

    if algorithm == "pomodoro":
        for t in tasks:
            remaining = t.duration_min
            while remaining > 0:
                dur = min(25, remaining)
                blocks.append({"task": t.title, "energy": t.energy, "start": now.isoformat(), "end": (now + timedelta(minutes=dur)).isoformat(), "algo": "pomodoro"})
                now += timedelta(minutes=dur)
                remaining -= dur
                if remaining > 0:
                    now += timedelta(minutes=5)  # short break
    elif algorithm == "flow_state":
        for t in tasks:
            dur = max(45, t.duration_min)
            blocks.append({"task": t.title, "energy": t.energy, "start": now.isoformat(), "end": (now + timedelta(minutes=dur)).isoformat(), "algo": "flow_state"})
            now += timedelta(minutes=dur + 10)
    else:  # time_blocking
        for t in tasks:
            dur = t.duration_min
            blocks.append({"task": t.title, "energy": t.energy, "start": now.isoformat(), "end": (now + timedelta(minutes=dur)).isoformat(), "algo": "time_blocking"})
            now += timedelta(minutes=dur)

    return {"algorithm": algorithm, "blocks": blocks}
