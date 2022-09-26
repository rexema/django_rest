import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';

function NaviBar() {
    return (
  <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">Menu</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Users</Nav.Link>
            <Nav.Link href="#pricing">Projects</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}
export default  NaviBar


