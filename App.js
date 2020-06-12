import React from 'react';
// import logo from './components/logo.png';
import './App.css';
import Questions from './components/Questions';

// import Questions from './components/Questions';
import NavBar from './components/NavBar';
// import Register from './components/Register';

function App() {

  return (
    <div className="App">
      {/* <header className="App-header"> */}
      <logo />
      <NavBar />
      <Questions />
      {/* </header> */}
    </div>

  );

}
export default App;
