// App.js
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route } from 'react-router';
import Sidebar from './components/sideBar';
import Control from './components/Control';
import Camera from './components/Camera';
import Log from './components/Log';
import Home from './components/Home';

const App = () => {
  return (
    <>
      <Sidebar/>
      <Routes>
        <Route path='/control' element={<Control/>} />
        <Route path='/camera' element={<Camera/>}/>
        <Route path='/log' element={<Log/>}/>
        <Route path='/' element={<Home/>}/>
      </Routes>
    </>
  );
}

export default App;
