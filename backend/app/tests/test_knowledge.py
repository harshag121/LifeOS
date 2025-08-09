from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest

@pytest.mark.asyncio
async def test_knowledge_graph():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Add two nodes and an edge
        r1 = await ac.post("/api/knowledge/node", json={"type":"concept","label":"Flow"})
        r2 = await ac.post("/api/knowledge/node", json={"type":"resource","label":"Deep Work"})
        assert r1.status_code == 200 and r2.status_code == 200
        n1, n2 = r1.json(), r2.json()
        e = await ac.post("/api/knowledge/edge", json={"source": n1["id"], "target": n2["id"], "relation":"influences"})
        assert e.status_code == 200
        g = await ac.get("/api/knowledge/graph")
        data = g.json()
        assert len(data["nodes"]) >= 2 and len(data["edges"]) >= 1
