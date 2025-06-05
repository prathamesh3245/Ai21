// src/App.jsx

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import ChatPage from "./pages/ChatPage";
import UploadForm from "./pages/UploadForm";
import QueryForm from "./pages/QueryForm";
import './App.css'

const App = () => {
  return (
    
    <Router>
     
      <div className="flex ">
      <div className="logo"></div>
        <Sidebar />
        <div className="flex-1 p-6">
          <Routes>
            <Route path="/" element={<ChatPage />} />
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/upload" element={<UploadForm />} />
            <Route path="/ask" element={<QueryForm />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;

