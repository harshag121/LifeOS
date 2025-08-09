# LifeOS

A fast, scalable, and beautiful personal operating system prototype.

## Stack
- Backend: FastAPI + SQLModel (SQLite local, Postgres in Docker)
- Frontend: Next.js (optional SPA at :3000) + server-rendered page at :8000
- Local models: TF‑IDF stored in `data/models/`

## Run locally

Backend only:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```
Open http://localhost:8000

Docker (API + Postgres + Web):
```bash
docker compose up --build
```
- API: http://localhost:8000
- Web: http://localhost:3000

## Tests
```bash
source .venv/bin/activate
pytest -q
```

## Features
- Adaptive UI (responsive), Neurosync AI (local), Smart Task Engine, Scheduler, Knowledge Graph, Insights, Wealth, Vital, Ideas.

## Next
- Rich SPA dashboard (3D graph), auth/permissions, audit views, migrations.