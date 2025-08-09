from httpx import AsyncClient, ASGITransport
from backend.app.main import app
import pytest
import uuid

@pytest.mark.asyncio
async def test_register_login():
    transport = ASGITransport(app=app)
    unique_email = f"user-{uuid.uuid4().hex[:8]}@example.com"
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post('/api/auth/register', json={"email": unique_email, "password": "secret"})
        assert r.status_code == 200
        token = r.json().get('access_token')
        assert token
        r2 = await ac.post('/api/auth/login', json={"email": unique_email, "password": "secret"})
        assert r2.status_code == 200
        assert r2.json().get('access_token')
