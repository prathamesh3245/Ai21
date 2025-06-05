// ChatPage.jsx
import React, { useState } from "react";
import axios from "axios";

const ChatPage = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);


  const handleAskQuestion = async () => {
    if (!question.trim()) {
      return;
    }
  
    setLoading(true);
    setAnswer(""); // Reset the answer before fetching
  
    try {
      const response = await axios.post("http://localhost:5000/chat", {
        question,
      });
  
      console.log("Response from backend:", response.data); // ✅ ADD THIS
  
      setAnswer(response.data?.data?.ai_response || "Sorry, I couldn't find an answer.");
    } catch (error) {
      console.error("Error querying the question", error);
      setAnswer("There was an error with the request.");
    } finally {
      setLoading(false);
    }
  };
  

  
  return (
    <div className="chat-container">
      <h2>Chat with the Bot</h2>
      <div className="chat-box">
        <div className="chat-box-header">
          <p>Ask me something!</p>
        </div>
        <div className="chat-box-body">
          {loading ? (
            <p>Loading...</p>
          ) : (
            <p>{answer ? answer : "Your answer will appear here."}</p>
          )}
        </div>
      </div>

      <div className="input-container">
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Type your question here..."
        />
        <button onClick={handleAskQuestion} disabled={loading}>
          Ask
        </button>
      </div>
    </div>
  );
};

export default ChatPage;
