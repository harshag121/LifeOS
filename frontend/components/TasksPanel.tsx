"use client";
import React, { useState, useEffect } from 'react';

type Task = { id?: number; title: string; energy: 'mental'|'physical'|'creative'; duration_min: number; deadline?: string|null };

export default function TasksPanel() {
  const [title, setTitle] = useState('');
  const [energy, setEnergy] = useState<'mental'|'physical'|'creative'>('mental');
  const [duration, setDuration] = useState(30);
  const [tasks, setTasks] = useState<Task[]>([]);

  const refresh = async () => {
    const r = await fetch('/api/tasks/list');
    setTasks(await r.json());
  };

  useEffect(()=>{ refresh(); },[]);

  const create = async () => {
    await fetch('/api/tasks/create', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ title, energy, duration_min: duration, depends_on: [] })});
    setTitle(''); setDuration(30);
    await refresh();
  };

  const prioritize = async () => {
    const r = await fetch('/api/tasks/prioritize');
    setTasks(await r.json());
  };

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-2">Tasks</h2>
      <input className="input mb-2" placeholder="Task title" value={title} onChange={e=>setTitle(e.target.value)} />
      <select className="select mb-2" value={energy} onChange={e=>setEnergy(e.target.value as any)}>
        <option value="mental">mental</option>
        <option value="physical">physical</option>
        <option value="creative">creative</option>
      </select>
      <input className="input mb-2" type="number" placeholder="Duration (min)" value={duration} onChange={e=>setDuration(parseInt(e.target.value || '0'))} />
      <div className="flex gap-2 mb-2">
        <button className="btn" onClick={create}>Add</button>
        <button className="btn" onClick={prioritize}>Prioritize</button>
      </div>
      <pre className="pre">{JSON.stringify(tasks, null, 2)}</pre>
    </div>
  );
}
