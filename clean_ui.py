import os

# 1. Login.tsx (Clean & Simple)
with open("frontend/src/pages/Login.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Shield } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4 font-sans text-gray-900">
      <div className="max-w-md w-full bg-white rounded-xl shadow-sm border border-gray-200 p-8">
        <div className="flex flex-col items-center mb-8">
          <Shield className="w-12 h-12 text-blue-600 mb-4" />
          <h1 className="text-2xl font-bold text-gray-900">Sentinel Security</h1>
          <p className="text-gray-500 mt-1 text-sm">Sign in to your account</p>
        </div>

        <form onSubmit={(e) => { e.preventDefault(); navigate('/dashboard'); }} className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input 
              type="email" 
              required
              className="w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors"
              placeholder="admin@example.com"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
            <input 
              type="password" 
              required
              className="w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors"
              placeholder="••••••••"
            />
          </div>
          <button 
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg px-4 py-2.5 text-sm font-medium transition-colors"
          >
            Sign In
          </button>
        </form>
      </div>
    </div>
  );
}
""")

# 2. DashboardLayout.tsx (Classic Enterprise Sidebar)
with open("frontend/src/layouts/DashboardLayout.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Outlet, Link, useLocation } from 'react-router-dom';
import { Shield, AlertTriangle, Activity, Server, Users, Lock, LogOut } from 'lucide-react';

export default function DashboardLayout() {
  const location = useLocation();
  const path = location.pathname;

  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: Activity },
    { name: 'Alerts', path: '/alerts', icon: AlertTriangle },
    { name: 'Applications', path: '/applications', icon: Server },
    { name: 'Policies', path: '/policies', icon: Lock },
    { name: 'Team', path: '/team', icon: Users },
  ];

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 font-sans flex">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 text-white flex flex-col hidden md:flex">
        <div className="p-5 flex items-center space-x-3 border-b border-slate-800">
          <Shield className="w-8 h-8 text-blue-500" />
          <h1 className="text-xl font-bold">Sentinel</h1>
        </div>
        
        <nav className="flex-1 p-4 space-y-1 overflow-y-auto">
          <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3 px-3">Main Menu</p>
          {navItems.map((item) => {
            const isActive = path.startsWith(item.path);
            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-blue-600 text-white font-medium'
                    : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                }`}
              >
                <item.icon className="w-5 h-5" />
                <span className="text-sm">{item.name}</span>
              </Link>
            )
          })}
        </nav>

        <div className="p-4 border-t border-slate-800">
          <Link to="/login" className="flex items-center space-x-3 px-3 py-2.5 rounded-lg text-slate-300 hover:bg-slate-800 transition-colors">
            <LogOut className="w-5 h-5" />
            <span className="text-sm">Log Out</span>
          </Link>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col min-h-screen overflow-hidden">
        {/* Header */}
        <header className="bg-white border-b border-gray-200 h-16 flex items-center justify-between px-8 shrink-0">
          <h2 className="text-lg font-semibold text-gray-800">
            {navItems.find(i => path.startsWith(i.path))?.name || 'Overview'}
          </h2>
          <div className="flex items-center space-x-4">
            <div className="text-right hidden sm:block">
              <p className="text-sm font-semibold text-gray-900">Admin User</p>
              <p className="text-xs text-gray-500">Security Team</p>
            </div>
            <div className="w-9 h-9 bg-blue-50 text-blue-700 rounded-full flex items-center justify-center font-bold border border-blue-200 cursor-pointer hover:bg-blue-100 transition-colors">
              A
            </div>
          </div>
        </header>

        {/* Workspace */}
        <div className="flex-1 overflow-y-auto p-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
""")

# 3. Dashboard.tsx (Clean Cards & Simple Chart)
with open("frontend/src/pages/Dashboard.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
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
""")

# 4. Applications.tsx (Clean Tables)
with open("frontend/src/pages/Applications.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Plus, Search } from 'lucide-react';

export default function Applications() {
  const apps = [
    { id: 1, name: 'Payment Gateway', env: 'Production', risk: 'Critical', status: 'Active' },
    { id: 2, name: 'Customer Portal', env: 'Production', risk: 'High', status: 'Active' },
    { id: 3, name: 'Admin Dashboard', env: 'Staging', risk: 'Medium', status: 'Maintenance' },
    { id: 4, name: 'Marketing Site', env: 'Production', risk: 'Low', status: 'Active' },
  ];

  return (
    <div className="max-w-7xl mx-auto animate-in fade-in duration-300">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Applications</h2>
        <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2.5 rounded-lg text-sm font-medium transition-colors flex items-center shadow-sm">
          <Plus className="w-4 h-4 mr-1.5" /> Add Application
        </button>
      </div>

      <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
        <div className="p-4 border-b border-gray-200 bg-gray-50/50">
          <div className="relative max-w-md">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input 
              type="text" 
              placeholder="Search applications..." 
              className="w-full border border-gray-300 text-gray-900 rounded-lg pl-9 pr-4 py-2 text-sm focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 bg-white"
            />
          </div>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-gray-50 border-b border-gray-200 text-gray-500 text-xs uppercase tracking-wider">
                <th className="px-6 py-3 font-medium">Application Name</th>
                <th className="px-6 py-3 font-medium">Environment</th>
                <th className="px-6 py-3 font-medium">Risk Level</th>
                <th className="px-6 py-3 font-medium">Status</th>
                <th className="px-6 py-3 font-medium text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 bg-white">
              {apps.map((app) => (
                <tr key={app.id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-sm font-semibold text-gray-900">{app.name}</td>
                  <td className="px-6 py-4 text-sm text-gray-500">{app.env}</td>
                  <td className="px-6 py-4">
                    <span className={`inline-flex px-2.5 py-1 rounded-full text-xs font-semibold border ${
                      app.risk === 'Critical' ? 'bg-red-50 text-red-700 border-red-200' :
                      app.risk === 'High' ? 'bg-orange-50 text-orange-700 border-orange-200' :
                      app.risk === 'Medium' ? 'bg-yellow-50 text-yellow-700 border-yellow-200' :
                      'bg-green-50 text-green-700 border-green-200'
                    }`}>
                      {app.risk}
                    </span>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center space-x-2">
                      <div className={`w-2 h-2 rounded-full ${app.status === 'Active' ? 'bg-green-500' : 'bg-yellow-500'}`}></div>
                      <span className="text-sm text-gray-700">{app.status}</span>
                    </div>
                  </td>
                  <td className="px-6 py-4 text-sm font-medium text-right">
                    <button className="text-blue-600 hover:text-blue-900 transition-colors">Edit</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
""")
