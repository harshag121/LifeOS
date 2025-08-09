from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlmodel import select
from backend.app.core.db import get_session
from backend.app.models.entities import User, AuditLog
from backend.app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()

class RegisterIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/register")
async def register(payload: RegisterIn, session=Depends(get_session)):
    existing = session.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    session.add(user)
    session.add(AuditLog(actor=payload.email, action="auth.register", meta=""))
    session.commit()
    session.refresh(user)
    token = create_access_token(subject=user.email)
    return TokenOut(access_token=token)

class LoginIn(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
async def login(payload: LoginIn, session=Depends(get_session)):
    user = session.exec(select(User).where(User.email == payload.email)).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    session.add(AuditLog(actor=payload.email, action="auth.login", meta=""))
    session.commit()
    token = create_access_token(subject=user.email)
    return TokenOut(access_token=token)
