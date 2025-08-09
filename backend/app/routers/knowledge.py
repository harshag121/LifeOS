from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Literal
from sqlmodel import select
from backend.app.core.db import get_session
from backend.app.models.entities import KGNode, KGEdge, AuditLog

router = APIRouter()

NodeType = Literal["concept", "resource", "person", "project"]

class Node(BaseModel):
    type: NodeType
    label: str

class Edge(BaseModel):
    source: int
    target: int
    relation: str

@router.post("/node")
async def add_node(n: Node, session=Depends(get_session)):
    node = KGNode(type=n.type, label=n.label)
    session.add(node)
    session.add(AuditLog(actor="system", action="kg.node", meta=n.label))
    session.commit()
    session.refresh(node)
    return node

@router.post("/edge")
async def add_edge(e: Edge, session=Depends(get_session)):
    edge = KGEdge(source=e.source, target=e.target, relation=e.relation)
    session.add(edge)
    session.add(AuditLog(actor="system", action="kg.edge", meta=f"{e.source}->{e.target}:{e.relation}"))
    session.commit()
    session.refresh(edge)
    return edge

@router.get("/graph")
async def graph(session=Depends(get_session)):
    nodes = session.exec(select(KGNode)).all()
    edges = session.exec(select(KGEdge)).all()
    return {"nodes": nodes, "edges": edges}
