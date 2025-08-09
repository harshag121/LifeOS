"use client";
import React, { useState } from 'react';

export default function NeurosyncPanel() {
  const [text, setText] = useState('');
  const [reply, setReply] = useState('');
  const [loading, setLoading] = useState(false);

  const send = async () => {
    setLoading(true);
    try {
      const r = await fetch('/api/neurosync/query', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ text })});
      const data = await r.json();
      setReply(JSON.stringify(data, null, 2));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-2">Neurosync</h2>
      <textarea className="textarea mb-2" rows={3} placeholder="Ask something..." value={text} onChange={e=>setText(e.target.value)} />
      <button className="btn" onClick={send} disabled={loading}>{loading? 'Sending...' : 'Send'}</button>
      <pre className="pre mt-2">{reply}</pre>
    </div>
  );
}
