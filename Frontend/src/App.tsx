import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import './App.css';

import InputPage from './ui/InputPage';
import ResultPage from './ui/ResultPage';

const App: React.FC = () => {
  const [emailContent, setEmailContent] = useState<string>('');
  const [spamProbability, setSpamProbability] = useState<number | null>(null);
  const url = import.meta.env.VITE_API_URL

  const resetEmailContent = () => {
    setEmailContent('')
  };

  const checkSpamRisk = async (content: string) => {
    try {
      console.log('Email content being sent:', content);
      console.log('url', url)
      const response = await axios.post(`${url}/api/predict`, {
        email: content,
      });
      console.log('Response from Flask API:', response);
      if (response.data && response.data.spam_prob !== undefined) {
        setSpamProbability(response.data.spam_prob);
      } else {
        console.error('Unexpected response structure:', response.data);
        setSpamProbability(null);
      }
    } catch (error) {
      console.error('Error checking spam risk:', error);
      setSpamProbability(null);
    }
  };

  return (
    <Router>
      <div className="App">
        <h1>Email Spam Detector</h1>
        <Routes>
          <Route
            path="/"
            element={<InputPage setEmailContent={setEmailContent} checkSpamRisk={checkSpamRisk} />}
          />
          <Route
            path="/result"
            element={<ResultPage emailContent={emailContent} spamProbability={spamProbability} resetEmailContent={resetEmailContent} />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
