"use client";
import React, { useState } from 'react';
import NeurosyncPanel from '../components/NeurosyncPanel';
import TasksPanel from '../components/TasksPanel';
import KnowledgePanel from '../components/KnowledgePanel';
import SchedulerPanel from '../components/SchedulerPanel';
import InsightsPanel from '../components/InsightsPanel';

export default function Home() {
  const [status, setStatus] = useState<string>("unknown");
  const [loading, setLoading] = useState(false);

  const checkHealth = async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/health');
      const data = await res.json();
      setStatus(data.status || 'unknown');
    } catch (e) {
      setStatus('error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="container py-6">
      <h1 className="text-3xl font-bold">LifeOS</h1>
      <p className="text-slate-300">Adaptive UI • Neurosync AI • Smart Task Engine • Knowledge Graph • Scheduler • Insights</p>
      <div className="mt-3">
        <button onClick={checkHealth} className="btn">Check API Health</button>
        <span className="ml-3">{loading ? 'Checking…' : `Status: ${status}`}</span>
      </div>
      <section className="grid-auto mt-6">
        <NeurosyncPanel />
        <TasksPanel />
        <KnowledgePanel />
        <SchedulerPanel />
        <InsightsPanel />
      </section>
    </main>
  )
}
