import React, { useState, ChangeEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

interface InputPageProps {
  setEmailContent: React.Dispatch<React.SetStateAction<string>>;
  checkSpamRisk: (emailContent: string) => void;
}

const InputPage: React.FC<InputPageProps> = ({ setEmailContent, checkSpamRisk }) => {
  const [localEmailContent, setLocalEmailContent] = useState('');
  const navigate = useNavigate();

  const handleTextChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    const value = e.target.value;
    setLocalEmailContent(value); 
    setEmailContent(value);
  };

  const handleSubmit = () => {
    if (!localEmailContent.trim()) {
      toast.error('Email content is empty! Please insert the message.', {
        position: 'top-center',
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        theme: 'colored',
      });
      return;
    }
    checkSpamRisk(localEmailContent);
    navigate('/result') 
  };

  return (
    <div>
      <h2>Enter Email Content</h2>
      <textarea
        rows={10}
        cols={50}
        onChange={handleTextChange}
        placeholder="Write your email content here"
      />
      <br />
      <button onClick={handleSubmit}>Check for Spam</button>
      <ToastContainer />
    </div>
  );
};

export default InputPage;