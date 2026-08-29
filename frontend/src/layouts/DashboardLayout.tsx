import React from 'react';
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
