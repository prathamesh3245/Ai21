import React, { useState } from 'react';
import axios from 'axios';

const QueryForm = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleQueryChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleQuerySubmit = async () => {
    if (!question) {
      setAnswer('Please enter a question!');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/ask', {
        question,
      });
      setAnswer(response.data.answer || 'No answer found.');
    } catch (error) {
      setAnswer('Error querying the PDF. Please try again.');
    }
  };

  return (
    <div>
      <h1>Ask a Question</h1>
      <input type="text" onChange={handleQueryChange} placeholder="Enter your question" />
      <button onClick={handleQuerySubmit}>Ask</button>
      <p>{answer}</p>
    </div>
  );
};

export default QueryForm;
