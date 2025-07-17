import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1 style={{ color: 'green' }}>✅ React is Working!</h1>
      <p>If you see this, your Nginx + React setup is good.</p>
    </div>
  );
}
export default App;






//   useEffect(() => {
//     axios.get('/api/hello')
//       .then(response => {
//         console.log("✅ Response:", response.data);
//         setMessage(response.data.message);
//       })
//       .catch(err => {
//         console.error("❌ Error fetching:", err);
//         setMessage("Error fetching message");
//       });
//   }, []);

//   return (
//     <div>
//       <h1>Zinad Frontend</h1>
//       <p>Message from backend: {message}</p>
//     </div>
//   );
// }


