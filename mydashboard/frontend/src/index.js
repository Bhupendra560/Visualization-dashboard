// myapp/frontend/src/index.js
// import React from 'react';
// import ReactDOM from 'react-dom';
// import App from './App';

// ReactDOM.render(<App />, document.getElementById('root'));

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';


// Replace ReactDOM.render with createRoot().render
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the app using the new createRoot API
root.render(<App />);