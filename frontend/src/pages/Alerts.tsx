import React from 'react';

export default function Alerts() {
  return (
    <div className="animate-in fade-in duration-500">
      <h2 className="text-2xl font-bold mb-6 text-gray-100">Security Alerts</h2>
      <div className="bg-gray-800 rounded-xl border border-gray-700 p-8 text-center text-gray-400 shadow-lg">
        <p className="text-lg">Alert Investigation Module is currently under construction.</p>
        <p className="mt-2 text-sm">Once the backend detection engine is fully hooked up, real-time alerts will stream here via WebSockets.</p>
      </div>
    </div>
  );
}
