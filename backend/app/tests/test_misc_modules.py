from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_wealth_vital_ideas():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        w = await ac.get("/api/wealth/summary")
        assert w.status_code == 200
        v = await ac.post("/api/vital/ingest", json={"hrv": 65})
        assert v.status_code == 200
        i = await ac.get("/api/ideas/boosters")
        assert i.status_code == 200
