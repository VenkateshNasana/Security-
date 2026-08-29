import os

# Create directories
dirs = [
    "frontend/src/layouts",
    "frontend/src/pages",
    "frontend/src/components"
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# 1. App.tsx
with open("frontend/src/App.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import DashboardLayout from './layouts/DashboardLayout';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Applications from './pages/Applications';
import Alerts from './pages/Alerts';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        
        {/* Protected Routes Wrapper (Mocked for now) */}
        <Route path="/" element={<DashboardLayout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="applications" element={<Applications />} />
          <Route path="alerts" element={<Alerts />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
""")

# 2. DashboardLayout.tsx
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
    <div className="min-h-screen bg-gray-900 text-white font-sans flex flex-col">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700 p-4 flex items-center justify-between sticky top-0 z-10">
        <div className="flex items-center space-x-3">
          <Shield className="w-8 h-8 text-blue-500" />
          <h1 className="text-xl font-bold tracking-wider">SENTINEL<span className="text-blue-500">WEB</span></h1>
        </div>
        <div className="flex items-center space-x-4">
          <span className="text-sm text-gray-400">Admin User</span>
          <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-sm font-bold cursor-pointer hover:bg-blue-500 transition">A</div>
          <Link to="/login" className="text-gray-400 hover:text-white transition">
            <LogOut className="w-5 h-5" />
          </Link>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside className="w-64 bg-gray-800 p-4 border-r border-gray-700 overflow-y-auto hidden md:block">
          <nav className="space-y-2">
            {navItems.map((item) => (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center space-x-3 p-3 rounded-lg transition ${
                  path.startsWith(item.path)
                    ? 'bg-blue-600/20 text-blue-400 border border-blue-500/30'
                    : 'text-gray-400 hover:bg-gray-700 hover:text-white'
                }`}
              >
                <item.icon className="w-5 h-5" />
                <span>{item.name}</span>
              </Link>
            ))}
          </nav>
        </aside>

        {/* Workspace */}
        <main className="flex-1 p-6 lg:p-8 bg-gray-900 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
""")

# 3. Dashboard.tsx
with open("frontend/src/pages/Dashboard.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { AlertTriangle, Activity, Server, Lock, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  return (
    <div className="animate-in fade-in duration-500">
      <h2 className="text-2xl font-bold mb-6 text-gray-100">Security Overview</h2>
      
      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-lg cursor-pointer hover:border-red-500 transition group">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-gray-400 font-medium group-hover:text-red-400 transition">Active Alerts</h3>
            <AlertTriangle className="w-6 h-6 text-red-500" />
          </div>
          <p className="text-3xl font-bold text-white">24</p>
          <p className="text-sm text-red-400 mt-2 flex items-center">↑ 12% Critical</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-lg cursor-pointer hover:border-blue-500 transition group">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-gray-400 font-medium group-hover:text-blue-400 transition">Events (24h)</h3>
            <Activity className="w-6 h-6 text-blue-500" />
          </div>
          <p className="text-3xl font-bold text-white">1.2M</p>
          <p className="text-sm text-green-400 mt-2 flex items-center">Normal traffic</p>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-lg cursor-pointer hover:border-purple-500 transition group">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-gray-400 font-medium group-hover:text-purple-400 transition">Monitored Apps</h3>
            <Server className="w-6 h-6 text-purple-500" />
          </div>
          <p className="text-3xl font-bold text-white">8</p>
          <p className="text-sm text-gray-400 mt-2 flex items-center">All systems healthy</p>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-lg cursor-pointer hover:border-green-500 transition group">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-gray-400 font-medium group-hover:text-green-400 transition">Active Policies</h3>
            <Lock className="w-6 h-6 text-green-500" />
          </div>
          <p className="text-3xl font-bold text-white">156</p>
          <p className="text-sm text-gray-400 mt-2 flex items-center">Fully enforced</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Recent Alerts */}
        <div className="bg-gray-800 rounded-xl border border-gray-700 shadow-lg flex flex-col">
          <div className="p-6 border-b border-gray-700 flex justify-between items-center">
            <h3 className="text-xl font-bold">Recent Critical Alerts</h3>
            <Link to="/alerts" className="text-blue-400 hover:text-blue-300 text-sm flex items-center transition">
              View All <ArrowRight className="w-4 h-4 ml-1" />
            </Link>
          </div>
          <div className="p-0 flex-1">
            <ul className="divide-y divide-gray-700">
              {[
                { id: 'ALT-992', title: 'Multiple Failed Logins', app: 'Payment Gateway', time: '2 mins ago' },
                { id: 'ALT-991', title: 'Suspicious API Pattern', app: 'Customer Portal', time: '15 mins ago' },
                { id: 'ALT-990', title: 'Privilege Escalation Attempt', app: 'Admin Panel', time: '1 hour ago' },
              ].map((alert) => (
                <li key={alert.id} className="p-4 hover:bg-gray-700/50 transition flex justify-between items-center cursor-pointer">
                  <div>
                    <p className="font-semibold text-red-400">{alert.title}</p>
                    <p className="text-sm text-gray-400">{alert.id} • {alert.app}</p>
                  </div>
                  <span className="text-xs text-gray-500">{alert.time}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Status Section */}
        <div className="bg-gray-800 rounded-xl border border-gray-700 p-6 shadow-lg">
          <h3 className="text-xl font-bold mb-6">System Health</h3>
          <div className="space-y-4">
            <div className="flex items-center space-x-4 p-4 bg-gray-900 rounded-lg border border-gray-700">
              <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse shadow-[0_0_10px_rgba(34,197,94,0.5)]"></div>
              <div>
                <p className="font-medium text-green-400">Event Ingestion Pipeline</p>
                <p className="text-sm text-gray-400">Processing ~500 events/sec</p>
              </div>
            </div>
            <div className="flex items-center space-x-4 p-4 bg-gray-900 rounded-lg border border-gray-700">
              <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse shadow-[0_0_10px_rgba(34,197,94,0.5)]"></div>
              <div>
                <p className="font-medium text-green-400">Detection Engine</p>
                <p className="text-sm text-gray-400">All rules active. Latency: 12ms</p>
              </div>
            </div>
            <div className="flex items-center space-x-4 p-4 bg-gray-900 rounded-lg border border-gray-700">
              <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse shadow-[0_0_10px_rgba(34,197,94,0.5)]"></div>
              <div>
                <p className="font-medium text-green-400">Database Connection</p>
                <p className="text-sm text-gray-400">PostgreSQL connected. Redis caching active.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
""")

# 4. Applications.tsx
with open("frontend/src/pages/Applications.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Plus, Search, MoreVertical } from 'lucide-react';

export default function Applications() {
  const apps = [
    { id: 1, name: 'Payment Gateway', env: 'Production', risk: 'Critical', status: 'Active' },
    { id: 2, name: 'Customer Portal', env: 'Production', risk: 'High', status: 'Active' },
    { id: 3, name: 'Admin Dashboard', env: 'Staging', risk: 'Medium', status: 'Maintenance' },
    { id: 4, name: 'Marketing Site', env: 'Production', risk: 'Low', status: 'Active' },
  ];

  return (
    <div className="animate-in fade-in duration-500">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-100">Registered Applications</h2>
        <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition shadow flex items-center">
          <Plus className="w-5 h-5 mr-1" /> Add Application
        </button>
      </div>

      <div className="bg-gray-800 rounded-xl border border-gray-700 shadow-lg overflow-hidden">
        <div className="p-4 border-b border-gray-700 flex space-x-4">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              type="text" 
              placeholder="Search applications..." 
              className="w-full bg-gray-900 border border-gray-700 text-white rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:border-blue-500 transition"
            />
          </div>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-gray-900/50 text-gray-400 text-sm">
                <th className="p-4 font-medium">Application Name</th>
                <th className="p-4 font-medium">Environment</th>
                <th className="p-4 font-medium">Risk Level</th>
                <th className="p-4 font-medium">Status</th>
                <th className="p-4 font-medium"></th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-700">
              {apps.map((app) => (
                <tr key={app.id} className="hover:bg-gray-700/50 transition">
                  <td className="p-4 font-medium text-white">{app.name}</td>
                  <td className="p-4 text-gray-400">{app.env}</td>
                  <td className="p-4">
                    <span className={`px-2 py-1 rounded text-xs font-bold ${
                      app.risk === 'Critical' ? 'bg-red-500/20 text-red-400' :
                      app.risk === 'High' ? 'bg-orange-500/20 text-orange-400' :
                      app.risk === 'Medium' ? 'bg-yellow-500/20 text-yellow-400' :
                      'bg-green-500/20 text-green-400'
                    }`}>
                      {app.risk}
                    </span>
                  </td>
                  <td className="p-4">
                    <span className="flex items-center space-x-2">
                      <span className={`w-2 h-2 rounded-full ${app.status === 'Active' ? 'bg-green-500' : 'bg-yellow-500'}`}></span>
                      <span className="text-gray-300">{app.status}</span>
                    </span>
                  </td>
                  <td className="p-4 text-right">
                    <button className="text-gray-400 hover:text-white transition p-1">
                      <MoreVertical className="w-5 h-5" />
                    </button>
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

# 5. Alerts.tsx
with open("frontend/src/pages/Alerts.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';

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
""")

# 6. Login.tsx
with open("frontend/src/pages/Login.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Shield } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    navigate('/dashboard');
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-gray-800 rounded-2xl shadow-2xl border border-gray-700 p-8 animate-in zoom-in-95 duration-300">
        <div className="flex flex-col items-center mb-8">
          <div className="w-16 h-16 bg-blue-600/20 rounded-full flex items-center justify-center mb-4">
            <Shield className="w-10 h-10 text-blue-500" />
          </div>
          <h1 className="text-3xl font-bold tracking-wider text-white">SENTINEL<span className="text-blue-500">WEB</span></h1>
          <p className="text-gray-400 mt-2">Security Monitoring Platform</p>
        </div>

        <form onSubmit={handleLogin} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">Email Address</label>
            <input 
              type="email" 
              required
              className="w-full bg-gray-900 border border-gray-700 text-white rounded-lg px-4 py-3 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition"
              placeholder="admin@sentinel.local"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">Password</label>
            <input 
              type="password" 
              required
              className="w-full bg-gray-900 border border-gray-700 text-white rounded-lg px-4 py-3 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition"
              placeholder="••••••••"
            />
          </div>
          <button 
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg px-4 py-3 font-bold transition shadow-lg shadow-blue-600/20"
          >
            Sign In to Dashboard
          </button>
        </form>
        
        <p className="mt-6 text-center text-sm text-gray-500">
          Demo Mode: Any credentials will work.
        </p>
      </div>
    </div>
  );
}
""")

print("React UI generated successfully.")
