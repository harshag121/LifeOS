from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_scheduler_suggest():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Ensure a task exists
        await ac.post("/api/tasks/create", json={"title":"Plan","energy":"mental","duration_min":30})
        r = await ac.get("/api/scheduler/suggest?algorithm=time_blocking")
        assert r.status_code == 200
        data = r.json()
        assert "blocks" in data and len(data["blocks"]) >= 1
