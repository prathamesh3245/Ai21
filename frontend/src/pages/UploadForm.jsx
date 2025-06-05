import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [responseMessage, setResponseMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setResponseMessage('Please choose a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponseMessage(response.data.message || 'File uploaded successfully!');
    } catch (error) {
      setResponseMessage('Error uploading file. Please try again.');
    }
  };

  return (
    <div>
      <h1>Upload PDF</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{responseMessage}</p>
    </div>
  );
};

export default UploadForm;
