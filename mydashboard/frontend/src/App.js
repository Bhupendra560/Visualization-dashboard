import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GridContainer from './components/GridContainer';
// import './components/ElevatedFrame.css';



// const App = () => {
//   const [apiData, setApiData] = useState([]);

//   useEffect(() => {
//     // Fetch your API data here using axios or any other method
//     // Example using placeholder API (JSONPlaceholder): https://jsonplaceholder.typicode.com/posts
//     axios.get('https://jsonplaceholder.typicode.com/posts')
//       .then(response => {
//         setApiData(response.data.slice(0, 8)); // Limit to the first 8 items
//       })
//       .catch(error => {
//         console.error('Error fetching API data:', error);
//       });
//   }, []);

//   return (
//     <div style={{ width: '100%', height: '100%', overflow: 'hidden' }}>
//       <GridContainer apiData={apiData} />
//     </div>
//   );
// };


const App = () => {
  const [apiData, setApiData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("/apis/news");
        const responseData = response.data.data;
        setApiData(responseData);
        console.log('API Response:', responseData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ width: '100%', height: '100%', overflow: 'hidden' }}>
      <GridContainer apiData={apiData} />
    </div>
  );
};


// const App = () => {
//   const [apiData, setApiData] = useState([]);

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         // Fetch data from the DRF API using axios
//         const response = await axios.get("/apis/news");
//         const responseData = response.data.data;
//         setApiData(responseData);
//         console.log('API Response:', responseData);
//       } catch (error) {
//         console.error('Error fetching data:', error);
//       }
//     };

//     fetchData();
//   }, []);

//   return (
//     <div style={{ width: '100%', height: '100%', overflow: 'hidden' }}>
//       {apiData.map((item, index) => (
//         <GridContainer key={index} title={item.title} description={item.description} />
//       ))}
//     </div>
//   );
// };



//   //   <div>
//   //     <h1>Data from DRF API:</h1>
//   //     <ul>
//   //       {apiData.map(item => (
//   //         <li key={item.id}>
//   //           {Object.entries(item).map(([key, value]) => (
//   //             <div key={key}>
//   //               <strong>{key}:</strong> {value}
//   //             </div>
//   //           ))}
//   //         </li>
//   //       ))}
//   //     </ul>
//   //   </div>
//   // );
// }

export default App;