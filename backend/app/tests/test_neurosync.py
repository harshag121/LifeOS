from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_neurosync():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/api/neurosync/query", json={"text": "Hello"})
        assert r.status_code == 200
        assert "reply" in r.json()
