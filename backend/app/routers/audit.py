from fastapi import APIRouter, Depends
from sqlmodel import select
from backend.app.core.db import get_session
from backend.app.models.entities import AuditLog

router = APIRouter()

@router.get("/recent")
async def recent(limit: int = 20, session=Depends(get_session)):
    logs = session.exec(select(AuditLog).order_by(AuditLog.id.desc()).limit(limit)).all()
    return logs
