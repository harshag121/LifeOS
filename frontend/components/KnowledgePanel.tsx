"use client";
import React, { useState, useEffect } from 'react';

type NodeType = 'concept'|'resource'|'person'|'project';

type Graph = { nodes: any[]; edges: any[] };

export default function KnowledgePanel() {
  const [label, setLabel] = useState('');
  const [type, setType] = useState<NodeType>('concept');
  const [graph, setGraph] = useState<Graph>({ nodes: [], edges: [] });

  const refresh = async () => {
    const g = await (await fetch('/api/knowledge/graph')).json();
    setGraph(g);
  };
  useEffect(()=>{ refresh(); },[]);

  const addNode = async () => {
    await fetch('/api/knowledge/node', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ type, label })});
    setLabel('');
    await refresh();
  };

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-2">Knowledge Graph</h2>
      <input className="input mb-2" placeholder="Node label" value={label} onChange={e=>setLabel(e.target.value)} />
      <select className="select mb-2" value={type} onChange={e=>setType(e.target.value as NodeType)}>
        <option>concept</option>
        <option>resource</option>
        <option>person</option>
        <option>project</option>
      </select>
      <button className="btn" onClick={addNode}>Add Node</button>
      <pre className="pre mt-2">{JSON.stringify(graph, null, 2)}</pre>
    </div>
  );
}
