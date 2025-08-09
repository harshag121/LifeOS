from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from .routers import health, neurosync, tasks, insights, knowledge
from .routers import scheduler, wealth, vital, ideas
from .routers import auth, audit
from .core.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="LifeOS", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple audit middleware placeholder (extend as needed)
@app.middleware("http")
async def audit_log(request: Request, call_next):
    response = await call_next(request)
    return response

app.include_router(health.router, prefix="/api")
app.include_router(neurosync.router, prefix="/api/neurosync")
app.include_router(tasks.router, prefix="/api/tasks")
app.include_router(insights.router, prefix="/api/insights")
app.include_router(knowledge.router, prefix="/api/knowledge")
app.include_router(scheduler.router, prefix="/api/scheduler")
app.include_router(wealth.router, prefix="/api/wealth")
app.include_router(vital.router, prefix="/api/vital")
app.include_router(ideas.router, prefix="/api/ideas")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(audit.router, prefix="/api/audit")

app.mount("/static", StaticFiles(directory="backend/app/static"), name="static")
templates = Jinja2Templates(directory="backend/app/templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
