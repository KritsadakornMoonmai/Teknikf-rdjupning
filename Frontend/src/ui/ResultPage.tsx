import React from 'react';
import { useNavigate } from 'react-router-dom';

interface ResultPageProps {
  emailContent: string;
  spamProbability: number | null;
  resetEmailContent: ()=> void;
}

const ResultPage: React.FC<ResultPageProps> = ({ emailContent, spamProbability, resetEmailContent }) => {
  const navigate = useNavigate();
  const handleGoBack = () => {
    resetEmailContent(); // Clear email content
    navigate('/'); // Navigate back to the input page
  };
    
  const renderResult = () => {
    if (spamProbability === null) {
      return <p>Loading result...</p>;
    }
    

    const isSpam = spamProbability >= 50;
    return (
      <div>
        <p>
          Your email content is:
        </p>
        <p>{emailContent}</p>
        <p>
          Spam Probability: <strong>{spamProbability.toFixed(2)}%</strong>
        </p>
        <p>{isSpam ? 'This email is likely spam based on the content.' : 'This email seems safe based on the content.'}</p>
        <button onClick={handleGoBack}>Go Back</button>
      </div>
    );
  };

  return (
    <div>
      <h2>Spam Detection Result</h2>
      {renderResult()}
    </div>
  );
}

export default ResultPage;