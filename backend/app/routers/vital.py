from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Biometrics(BaseModel):
    hrv: int
    sleep_stages: dict | None = None
    activity_levels: dict | None = None

@router.post("/ingest")
async def ingest(bio: Biometrics):
    recovery = min(100, int(bio.hrv * 1.2))
    return {"recovery_scores": recovery, "productivity_correlations": {"hrv": 0.6}}
