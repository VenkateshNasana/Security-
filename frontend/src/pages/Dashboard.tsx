import React from 'react';
import { AlertTriangle, Activity, Server, Lock } from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { time: '00:00', events: 4000, alerts: 24 },
  { time: '04:00', events: 3000, alerts: 13 },
  { time: '08:00', events: 8000, alerts: 55 },
  { time: '12:00', events: 12000, alerts: 89 },
  { time: '16:00', events: 9000, alerts: 42 },
  { time: '20:00', events: 6000, alerts: 30 },
  { time: '24:00', events: 4500, alerts: 28 },
];

export default function Dashboard() {
  return (
    <div className="max-w-7xl mx-auto animate-in fade-in duration-300">
      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider">Critical Alerts</h3>
            <div className="p-2 bg-red-50 text-red-600 rounded-lg"><AlertTriangle className="w-5 h-5" /></div>
          </div>
          <p className="text-3xl font-bold text-gray-900">24</p>
          <p className="text-sm text-red-600 mt-2 font-medium">+12% from yesterday</p>
        </div>
        
        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider">Events Analyzed</h3>
            <div className="p-2 bg-blue-50 text-blue-600 rounded-lg"><Activity className="w-5 h-5" /></div>
          </div>
          <p className="text-3xl font-bold text-gray-900">1.2M</p>
          <p className="text-sm text-gray-500 mt-2">Last 24 hours</p>
        </div>

        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider">Monitored Assets</h3>
            <div className="p-2 bg-purple-50 text-purple-600 rounded-lg"><Server className="w-5 h-5" /></div>
          </div>
          <p className="text-3xl font-bold text-gray-900">12</p>
          <p className="text-sm text-gray-500 mt-2">Active environments</p>
        </div>

        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider">Active Policies</h3>
            <div className="p-2 bg-green-50 text-green-600 rounded-lg"><Lock className="w-5 h-5" /></div>
          </div>
          <p className="text-3xl font-bold text-gray-900">156</p>
          <p className="text-sm text-green-600 mt-2 font-medium">100% enforcement</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Chart Section */}
        <div className="lg:col-span-2 bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
          <h3 className="text-lg font-bold text-gray-900 mb-6">Traffic & Threat Correlation</h3>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#f3f4f6" vertical={false} />
                <XAxis dataKey="time" stroke="#9ca3af" tick={{fill: '#6b7280', fontSize: 12}} axisLine={false} tickLine={false} />
                <YAxis stroke="#9ca3af" tick={{fill: '#6b7280', fontSize: 12}} axisLine={false} tickLine={false} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#ffffff', borderColor: '#e5e7eb', borderRadius: '8px', color: '#111827' }}
                />
                <Area type="monotone" dataKey="events" stroke="#3b82f6" strokeWidth={2} fillOpacity={0.1} fill="#3b82f6" />
                <Area type="monotone" dataKey="alerts" stroke="#ef4444" strokeWidth={2} fillOpacity={0.1} fill="#ef4444" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Recent Alerts List */}
        <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden flex flex-col">
          <div className="p-5 border-b border-gray-200">
            <h3 className="text-lg font-bold text-gray-900">Recent Alerts</h3>
          </div>
          <div className="flex-1 p-0">
            <ul className="divide-y divide-gray-100">
              {[
                { id: 'ALT-992', title: 'Multiple Failed Logins', app: 'Payment Gateway', time: '2m' },
                { id: 'ALT-991', title: 'Suspicious API Pattern', app: 'Customer Portal', time: '15m' },
                { id: 'ALT-990', title: 'Privilege Escalation', app: 'Admin Panel', time: '1h' },
                { id: 'ALT-989', title: 'Unusual Geo-Location', app: 'Payment Gateway', time: '3h' },
              ].map((alert) => (
                <li key={alert.id} className="p-4 hover:bg-gray-50 transition-colors cursor-pointer">
                  <div className="flex justify-between items-start mb-1">
                    <p className="font-semibold text-gray-900 text-sm">{alert.title}</p>
                    <span className="text-xs text-gray-500 whitespace-nowrap ml-2">{alert.time}</span>
                  </div>
                  <p className="text-xs text-gray-500">{alert.id} • {alert.app}</p>
                </li>
              ))}
            </ul>
          </div>
          <div className="p-4 border-t border-gray-200 bg-gray-50 text-center">
            <button className="text-sm font-medium text-blue-600 hover:text-blue-700">View All Alerts →</button>
          </div>
        </div>
      </div>
    </div>
  );
}
