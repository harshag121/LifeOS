from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.services.nlp import nlp

router = APIRouter()

class Query(BaseModel):
    text: str
    personality: str | None = None
    verbosity: str | None = None

@router.post("/query")
async def query(q: Query):
    related = nlp.most_similar(q.text)
    persona = q.personality or 'default'
    verbosity = q.verbosity or 'normal'
    if verbosity == 'concise':
        reply = f"[{persona}] {related}"
    else:
        reply = f"[{persona}] You said: {q.text}. Related: {related}"
    return {"reply": reply}
