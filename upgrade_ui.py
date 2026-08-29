import os

# 1. Login.tsx (High-End Glassmorphism)
with open("frontend/src/pages/Login.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Shield } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-slate-950">
      {/* Animated Background Gradients */}
      <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600/20 blur-[120px] rounded-full mix-blend-screen"></div>
      <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-purple-600/20 blur-[120px] rounded-full mix-blend-screen"></div>
      
      <div className="relative z-10 max-w-md w-full bg-slate-900/60 backdrop-blur-2xl rounded-3xl shadow-2xl border border-slate-700/50 p-10 animate-in fade-in slide-in-from-bottom-8 duration-700">
        <div className="flex flex-col items-center mb-10">
          <div className="w-20 h-20 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-blue-500/30 rotate-3 transition-transform hover:rotate-6">
            <Shield className="w-10 h-10 text-white -rotate-3" />
          </div>
          <h1 className="text-4xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">
            SENTINEL
          </h1>
          <p className="text-slate-400 mt-2 font-medium tracking-wide text-sm uppercase letter-spacing-2">Enterprise Security</p>
        </div>

        <form onSubmit={(e) => { e.preventDefault(); navigate('/dashboard'); }} className="space-y-6">
          <div>
            <input 
              type="email" 
              required
              className="w-full bg-slate-950/50 border border-slate-700 text-white rounded-xl px-5 py-4 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all placeholder:text-slate-500"
              placeholder="Email Address"
            />
          </div>
          <div>
            <input 
              type="password" 
              required
              className="w-full bg-slate-950/50 border border-slate-700 text-white rounded-xl px-5 py-4 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all placeholder:text-slate-500"
              placeholder="Password"
            />
          </div>
          <button 
            type="submit"
            className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white rounded-xl px-5 py-4 font-bold transition-all shadow-[0_0_20px_rgba(37,99,235,0.3)] hover:shadow-[0_0_30px_rgba(37,99,235,0.5)] active:scale-95"
          >
            Authenticate Identity
          </button>
        </form>
      </div>
    </div>
  );
}
""")

# 2. DashboardLayout.tsx (Sleek Sidebar)
with open("frontend/src/layouts/DashboardLayout.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { Outlet, Link, useLocation } from 'react-router-dom';
import { Shield, AlertTriangle, Activity, Server, Users, Lock, LogOut, Settings } from 'lucide-react';

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
    <div className="min-h-screen bg-slate-950 text-slate-50 font-sans flex flex-col">
      {/* Premium Header */}
      <header className="bg-slate-900/80 backdrop-blur-xl border-b border-slate-800 p-4 flex items-center justify-between sticky top-0 z-20">
        <div className="flex items-center space-x-3 ml-2">
          <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center shadow-lg shadow-blue-500/20">
            <Shield className="w-6 h-6 text-white" />
          </div>
          <h1 className="text-xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">
            SENTINEL
          </h1>
        </div>
        <div className="flex items-center space-x-6 mr-4">
          <div className="flex items-center space-x-3 border-r border-slate-700 pr-6">
            <div className="text-right">
              <p className="text-sm font-semibold text-white">Naga Venkatesh</p>
              <p className="text-xs text-blue-400">Chief Security Officer</p>
            </div>
            <div className="w-10 h-10 bg-slate-800 rounded-full border border-slate-700 flex items-center justify-center text-sm font-bold shadow-inner cursor-pointer hover:border-blue-500 transition">
              NV
            </div>
          </div>
          <Settings className="w-5 h-5 text-slate-400 hover:text-white cursor-pointer transition" />
          <Link to="/login" className="text-slate-400 hover:text-red-400 transition">
            <LogOut className="w-5 h-5" />
          </Link>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex flex-1 overflow-hidden relative">
        {/* Abstract Background for Workspace */}
        <div className="absolute top-0 left-0 w-full h-96 bg-gradient-to-b from-blue-900/10 to-transparent pointer-events-none"></div>

        {/* Sidebar */}
        <aside className="w-64 bg-slate-900/50 backdrop-blur-md p-4 border-r border-slate-800 overflow-y-auto hidden md:block z-10">
          <nav className="space-y-2 mt-4">
            <p className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-4 ml-3">Menu</p>
            {navItems.map((item) => {
              const isActive = path.startsWith(item.path);
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  className={`flex items-center space-x-3 p-3 rounded-xl transition-all duration-300 ${
                    isActive
                      ? 'bg-gradient-to-r from-blue-600/20 to-purple-600/10 text-blue-400 border border-blue-500/30 shadow-[0_0_15px_rgba(37,99,235,0.1)]'
                      : 'text-slate-400 hover:bg-slate-800/80 hover:text-white border border-transparent'
                  }`}
                >
                  <item.icon className={`w-5 h-5 ${isActive ? 'text-blue-400' : 'text-slate-400'}`} />
                  <span className="font-medium">{item.name}</span>
                </Link>
              )
            })}
          </nav>
        </aside>

        {/* Workspace */}
        <main className="flex-1 p-6 lg:p-10 overflow-y-auto z-10">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
""")

# 3. Dashboard.tsx (Recharts & High-End Cards)
with open("frontend/src/pages/Dashboard.tsx", "w", encoding="utf-8") as f:
    f.write("""import React from 'react';
import { AlertTriangle, Activity, Server, ShieldCheck, ArrowUpRight } from 'lucide-react';
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
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div className="flex justify-between items-center mb-10">
        <div>
          <h2 className="text-3xl font-extrabold text-white tracking-tight">Command Center</h2>
          <p className="text-slate-400 mt-1">Real-time threat monitoring & analytics</p>
        </div>
        <div className="flex space-x-3">
          <span className="flex items-center px-4 py-2 bg-green-500/10 text-green-400 border border-green-500/20 rounded-full text-sm font-bold shadow-[0_0_15px_rgba(34,197,94,0.1)]">
            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse mr-2"></span> System Optimal
          </span>
        </div>
      </div>
      
      {/* Glass Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
        <div className="bg-slate-900/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-xl relative overflow-hidden group hover:-translate-y-1 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-red-500/10 rounded-full blur-3xl group-hover:bg-red-500/20 transition-all"></div>
          <div className="flex justify-between items-center mb-6 relative z-10">
            <h3 className="text-slate-400 font-medium">Critical Alerts</h3>
            <div className="p-2.5 bg-red-500/10 border border-red-500/20 rounded-xl"><AlertTriangle className="w-5 h-5 text-red-400" /></div>
          </div>
          <div className="relative z-10">
            <p className="text-4xl font-extrabold text-white">24</p>
            <p className="text-sm text-red-400 mt-2 font-medium flex items-center"><ArrowUpRight className="w-4 h-4 mr-1" /> 12% vs last week</p>
          </div>
        </div>
        
        <div className="bg-slate-900/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-xl relative overflow-hidden group hover:-translate-y-1 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-full blur-3xl group-hover:bg-blue-500/20 transition-all"></div>
          <div className="flex justify-between items-center mb-6 relative z-10">
            <h3 className="text-slate-400 font-medium">Events Analyzed</h3>
            <div className="p-2.5 bg-blue-500/10 border border-blue-500/20 rounded-xl"><Activity className="w-5 h-5 text-blue-400" /></div>
          </div>
          <div className="relative z-10">
            <p className="text-4xl font-extrabold text-white">1.2M</p>
            <p className="text-sm text-blue-400 mt-2 font-medium flex items-center">Last 24 hours</p>
          </div>
        </div>

        <div className="bg-slate-900/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-xl relative overflow-hidden group hover:-translate-y-1 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-3xl group-hover:bg-purple-500/20 transition-all"></div>
          <div className="flex justify-between items-center mb-6 relative z-10">
            <h3 className="text-slate-400 font-medium">Monitored Assets</h3>
            <div className="p-2.5 bg-purple-500/10 border border-purple-500/20 rounded-xl"><Server className="w-5 h-5 text-purple-400" /></div>
          </div>
          <div className="relative z-10">
            <p className="text-4xl font-extrabold text-white">12</p>
            <p className="text-sm text-purple-400 mt-2 font-medium flex items-center">Across 3 environments</p>
          </div>
        </div>

        <div className="bg-slate-900/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-xl relative overflow-hidden group hover:-translate-y-1 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-green-500/10 rounded-full blur-3xl group-hover:bg-green-500/20 transition-all"></div>
          <div className="flex justify-between items-center mb-6 relative z-10">
            <h3 className="text-slate-400 font-medium">Defense Status</h3>
            <div className="p-2.5 bg-green-500/10 border border-green-500/20 rounded-xl"><ShieldCheck className="w-5 h-5 text-green-400" /></div>
          </div>
          <div className="relative z-10">
            <p className="text-4xl font-extrabold text-white">99.9%</p>
            <p className="text-sm text-green-400 mt-2 font-medium flex items-center">System Uptime</p>
          </div>
        </div>
      </div>

      {/* Chart Section */}
      <div className="bg-slate-900/80 backdrop-blur-xl rounded-3xl border border-slate-700/50 p-8 shadow-2xl mb-8 relative overflow-hidden">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-32 bg-blue-500/5 blur-3xl rounded-full pointer-events-none"></div>
        <h3 className="text-xl font-bold text-white mb-8 relative z-10">Traffic & Threat Correlation (24h)</h3>
        
        <div className="h-[350px] w-full relative z-10">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data} margin={{ top: 10, right: 30, left: -20, bottom: 0 }}>
              <defs>
                <linearGradient id="colorEvents" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.4}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
                <linearGradient id="colorAlerts" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#ef4444" stopOpacity={0.4}/>
                  <stop offset="95%" stopColor="#ef4444" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
              <XAxis dataKey="time" stroke="#64748b" tick={{fill: '#64748b', fontSize: 12}} axisLine={false} tickLine={false} />
              <YAxis stroke="#64748b" tick={{fill: '#64748b', fontSize: 12}} axisLine={false} tickLine={false} />
              <Tooltip 
                contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)' }}
                itemStyle={{ color: '#f8fafc', fontWeight: 'bold' }}
              />
              <Area type="monotone" dataKey="events" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorEvents)" activeDot={{r: 6, fill: '#3b82f6', stroke: '#0f172a', strokeWidth: 2}} />
              <Area type="monotone" dataKey="alerts" stroke="#ef4444" strokeWidth={3} fillOpacity={1} fill="url(#colorAlerts)" activeDot={{r: 6, fill: '#ef4444', stroke: '#0f172a', strokeWidth: 2}} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
""")
