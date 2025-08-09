from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthData(BaseModel):
    hrv: int | None = None
    sleep_hours: float | None = None
    activity_minutes: int | None = None

class ProductivityData(BaseModel):
    deep_work_hours: float | None = None
    tasks_completed: int | None = None

class FinanceData(BaseModel):
    learning_hours: float | None = None
    savings_rate: float | None = None  # 0..1

class CrossModuleInput(BaseModel):
    health: HealthData
    productivity: ProductivityData

@router.post("/cross")
async def cross_module_analysis(payload: CrossModuleInput):
    score = 0.0
    if payload.health.hrv:
        score += payload.health.hrv / 100.0
    if payload.health.sleep_hours:
        score += payload.health.sleep_hours / 8.0
    if payload.productivity.deep_work_hours:
        score += payload.productivity.deep_work_hours / 4.0
    alert = "predictive" if score > 2.0 else "opportunity"
    return {"health_productivity_correlation": round(score, 2), "alert": alert}

class LearningFinanceInput(BaseModel):
    finance: FinanceData

@router.post("/learning_financial_impact")
async def learning_financial_impact(payload: LearningFinanceInput):
    if payload.finance.learning_hours is None or payload.finance.savings_rate is None:
        return {"impact": 0.0, "alert": "anomaly"}
    impact = payload.finance.learning_hours * (payload.finance.savings_rate * 10)
    alert = "opportunity" if impact < 5 else "predictive"
    return {"impact": round(impact, 2), "alert": alert}
