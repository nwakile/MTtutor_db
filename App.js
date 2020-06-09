import React from 'react';
import logo from './components/logo.png';
import './App.css';
import Login from './components/Login';

// import Questions from './components/Questions';
import NavBar from './components/NavBar';
// import Register from './components/Register';

function App() {

  return (
    <div className="App">
      {/* <header className="App-header"> */}
      <logo />
      <NavBar />
      <Login />
      {/* </header> */}
    </div>

  );

}
export default App;
