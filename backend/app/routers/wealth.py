from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class WealthSummary(BaseModel):
    automation: list[str]
    subscriptions: list[str]
    read_only_mode: bool

@router.get("/summary")
async def summary():
    return WealthSummary(
        automation=["expense_categorization", "subscription_monitoring"],
        subscriptions=["Spotify", "Netflix"],
        read_only_mode=True,
    )
