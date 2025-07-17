import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('Loading...');
  const [error, setError] = useState(null);

  useEffect(() => {
    // Test frontend is working
    console.log('React App is mounting...');
    
    // Test backend connection
    axios.get('/api/hello')
      .then(response => {
        console.log('✅ Backend Response:', response.data);
        setMessage(response.data.message);
        setError(null);
      })
      .catch(err => {
        console.error('❌ Backend Error:', err);
        setError(err.message);
        setMessage('Failed to connect to backend');
      });
  }, []);

  return (
    <div style={{ 
      textAlign: 'center', 
      marginTop: '50px',
      padding: '20px',
      fontFamily: 'Arial, sans-serif'
    }}>
      <h1 style={{ color: '#2e7d32' }}>🚀 Zinad Fullstack App</h1>
      <p style={{ fontSize: '18px', marginBottom: '20px' }}>
        Frontend Status: <strong style={{ color: 'green' }}>✅ Working</strong>
      </p>
      
      <div style={{
        background: '#f5f5f5',
        padding: '20px',
        borderRadius: '8px',
        margin: '20px auto',
        maxWidth: '500px'
      }}>
        <h3>Backend Communication:</h3>
        <p><strong>Message:</strong> {message}</p>
        {error && (
          <p style={{ color: 'red' }}>
            <strong>Error:</strong> {error}
          </p>
        )}
      </div>
      
      <div style={{ marginTop: '30px', fontSize: '14px', color: '#666' }}>
        <p>If you see this page, your React app is successfully built and served by nginx.</p>
        <p>Check the browser console (F12) for detailed logs.</p>
      </div>
    </div>
  );
}

export default App;
