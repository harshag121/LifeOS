"use client";
import React, { useState } from 'react';

export default function InsightsPanel() {
  const [out, setOut] = useState('');

  const healthProductivity = async () => {
    const payload={health:{hrv:70,sleep_hours:7.5,activity_minutes:40},productivity:{deep_work_hours:2.5,tasks_completed:5}};
    const r= await fetch('/api/insights/cross',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    setOut(JSON.stringify(await r.json(),null,2));
  };

  const learningFinance = async () => {
    const payload={finance:{learning_hours:1.2,savings_rate:0.25}};
    const r= await fetch('/api/insights/learning_financial_impact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    setOut(JSON.stringify(await r.json(),null,2));
  };

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-2">Insights</h2>
      <div className="flex gap-2 mb-2">
        <button className="btn" onClick={healthProductivity}>Health x Productivity</button>
        <button className="btn" onClick={learningFinance}>Learning Financial Impact</button>
      </div>
      <pre className="pre">{out}</pre>
    </div>
  );
}
