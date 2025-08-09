from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_health():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.get("/api/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"
