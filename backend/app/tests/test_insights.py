from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_insights_endpoints():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/api/insights/cross", json={
            "health": {"hrv": 70, "sleep_hours": 7.0, "activity_minutes": 40},
            "productivity": {"deep_work_hours": 2.5, "tasks_completed": 5}
        })
        assert r.status_code == 200
        data = r.json()
        assert "health_productivity_correlation" in data
        r2 = await ac.post("/api/insights/learning_financial_impact", json={
            "finance": {"learning_hours": 1.0, "savings_rate": 0.25}
        })
        assert r2.status_code == 200
        assert "impact" in r2.json()
