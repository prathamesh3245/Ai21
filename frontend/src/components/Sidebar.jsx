// src/components/Sidebar.jsx

import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="w-64 h-screen bg-gray-900 text-white p-6">
      <h1 className="text-2xl font-bold mb-8">Ai21Labs</h1>
      <nav className="flex flex-col space-y-4">
        <Link to="/chat" className="hover:text-blue-400">🗨️ Chat</Link>
        <Link to="/upload" className="hover:text-blue-400">📄 Upload File</Link>
        <Link to="/ask" className="hover:text-blue-400">❓ Ask from File</Link>
      </nav>
    </div>
  );
};

export default Sidebar;
