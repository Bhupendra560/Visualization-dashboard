import React from 'react';

const GridItem = ({ data }) => (
  <div
    style={{
      paddingLeft: '50px',
      paddingRight: '16px',
      border: '1px solid #ccc',
      borderRadius: '8px',
      padding: '16px',
      boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
      width: '260px',
      height: '200px',
    }}
  >

    <h2>{data.sector}</h2>
    <h4>{data.title}</h4>
    
  </div>
);



const GridContainer = ({ apiData }) => (

  <div
    style={{
      gap: '16px',
      display: 'flex',
      flexWrap: 'wrap',
      paddingLeft: '16px',
      paddingRight: '16px',
      paddingTop: '100px',
      justifyContent: 'center', 
      border: '3px solid #ccc',
      
    }}
  >
    {apiData.map((data, index) => (
     

      <GridItem key={index} data={data}/>

     
     
    ))}
  </div>
);







// const GridContainer = ({ apiData }) => {
//   console.log('apiData:', apiData);

//   return (
//     <div
//       style={{
//         display: 'grid',
//         gridTemplateColumns: 'repeat(auto-fill, minmax(100px, 1fr))',
//         gap: '20px',
//         padding: '30px',
//       }}
//     >
//       {apiData ? (
//         <GridItem title={apiData} />
//       ) : null }
//     </div>
//   );
// };


export default GridContainer;