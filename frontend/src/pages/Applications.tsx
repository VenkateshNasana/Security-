import React from 'react';
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
