from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_tasks_flow():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        new = {"title":"Write spec","energy":"mental","duration_min":25,"depends_on":[]}
        r = await ac.post("/api/tasks/create", json=new)
        assert r.status_code == 200
        listed = await ac.get("/api/tasks/list")
        assert listed.status_code == 200
        assert len(listed.json()) >= 1
        pr = await ac.get("/api/tasks/prioritize")
        assert pr.status_code == 200
