import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Navbar  from './components/Navbar';
import BasicExample from './components/login';
import Card from "./components/Card";
import Container from "react-bootstrap/esm/Container";
import Row from 'react-bootstrap/esm/Row';
import Col from 'react-bootstrap/esm/Col';

// import { ClienteLayout } from "./Layout";
// import { Navigation } from "./Routes/Navigation";


function App() {
  return (
  
    <Router>
      <Navbar/>
      <div className="container">
          <hr/>
        <Routes>
        <Route path="/" element={
          <Container>
            <Row>
              <Col xs={12} md={8}>
                <Card/> 
                <br></br>
                <Card/>
              </Col>
            </Row>
            <Row>
              <Col xs={6} md={4}>
                <Card/>
              </Col>
            </Row>
          </Container>
        }/>
        <Route path="/admin" element={<h1>Admin</h1>}/>
        <Route path="/login" element={<BasicExample/>}/>
        </Routes>
      </div>
    </Router>
    
  );
}

export default App;


// // import React from "react";
// // import {Container, Row, Col, Card, Form, Button } from "react-bootstrap";
// // import { withRouter } from "react-router";

// // import './Styles/App.css'

// const Dash = props => {
   

//     return (
//         <>
//          <Container fluid>
//                 <Row>
//                     <Col xs={2} id="sidebar-wrapper">      
//                       <Sidebar />
//                     </Col>
//                     <Col  xs={10} id="page-content-wrapper">
//                         this is a test
//                     </Col> 
//                 </Row>

//             </Container>
//         </>
//         );
//   };
//   const Dashboard = BrowserRouter(Dash);
//   export default Dashboard

