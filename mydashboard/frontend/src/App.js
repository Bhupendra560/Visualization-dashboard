import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [apiData, setApiData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch data from the DRF API using axios
        const response = await axios.get("/apis/news");
        const responseData = response.data.data; // Store response in a variable
        setApiData(responseData);
        console.log('API Response:', responseData);
        
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Data from DRF API:</h1>
      <ul>
        {apiData.map(item => (
          <li key={item.id}>
            {Object.entries(item).map(([key, value]) => (
              <div key={key}>
                <strong>{key}:</strong> {value}
              </div>
            ))}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;