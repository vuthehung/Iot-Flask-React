import React from 'react';
import { NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function SideBar() {
  return (
    
    <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary">
      <Container>
        <NavLink to='/' className='text-decoration-none navbar-brand'><strong>Trang chủ</strong></NavLink>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <NavLink to="/control" className="nav-link">Điều khiển</NavLink>
            <NavLink to="/log" className="nav-link">Lịch sử</NavLink>
            <NavLink to="/camera" className="nav-link">Camera</NavLink>
          </Nav>
          <Nav>
            <NavLink to="account" className="nav-link">Xin chào, Hùng</NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default SideBar;