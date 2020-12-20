import React from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
} from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

import "./App.css";
import Home from "./Home";

export default function App() {
    return (
        <div className="App">
            <Navbar bg="light" expand="lg">
                <Navbar.Brand>Cyber Punks</Navbar.Brand>
                
                <Navbar.Toggle aria-controls="basic-navbar-nav" />

                <Navbar.Collapse id="navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Item>
                            <Link to="/">Home</Link>
                        </Nav.Item>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

            <Switch>
                <Route path="/">
                    <Home />
                </Route>
            </Switch>
        </div>
    );
}
