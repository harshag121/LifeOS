"use client";
import React, { useState } from 'react';

type Algo = 'time_blocking'|'pomodoro'|'flow_state';

export default function SchedulerPanel() {
  const [algo, setAlgo] = useState<Algo>('time_blocking');
  const [blocks, setBlocks] = useState<any>(null);

  const suggest = async () => {
    const r = await fetch(`/api/scheduler/suggest?algorithm=${algo}`);
    setBlocks(await r.json());
  };

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-2">Scheduler</h2>
      <select className="select mb-2" value={algo} onChange={e=>setAlgo(e.target.value as Algo)}>
        <option>time_blocking</option>
        <option>pomodoro</option>
        <option>flow_state</option>
      </select>
      <button className="btn" onClick={suggest}>Suggest Blocks</button>
      <pre className="pre mt-2">{JSON.stringify(blocks, null, 2)}</pre>
    </div>
  );
}
