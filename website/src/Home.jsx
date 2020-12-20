import React, { useState } from "react";
import styled from "styled-components";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Spinner from "react-bootstrap/Spinner";
import Card from "react-bootstrap/Card";

import logo from "./logo.jpg";

const HomeDiv = styled.div`
padding: 20px;
`;

const LogoImg = styled.img`
width: 300px;
`;

/**
 * Displays a get content form and handles calling the get content endpoint.
 * @params props.setContent State setter for the content state. Takes the root content
 *     node object as a value.
 */
function GetContent(props) {
    const setContent = props.setContent;

    const [source, setSource] = useState("https://reddit.com/r/dogs");
    const [isLoading, setIsLoading] = useState(false);
    
    const onSubmit = async (e) => {
        e.preventDefault();

        if (source.length === 0) {
            alert("Must enter a source URL");
            return;
        }

        // Get content
        setIsLoading(true);

        const resp = await fetch("http://localhost:8180/api/analyse", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                source: source,
            }),
        });
        const body = await resp.json();
        
        setIsLoading(false);
        setContent(body);
    };

    let body = (
        <Form onSubmit={onSubmit}>
            <Form.Group controlId="contentUri">
                <Form.Label>Content URL</Form.Label>
                <Form.Control
                    value={source}
                    type="text"
                    placeholder="https://reddit.com"
                    onChange={(e) => {
                        setSource(e.target.value);
                    }}
                />
            </Form.Group>

            <Button variant="primary" type="submit">
                View Content
            </Button>
        </Form>
    );

    if (isLoading === true) {
        body = (
            <div>
                <Spinner animation="border" />
            </div>
        );
    }
    
    return (
        <>
            <LogoImg src={logo} />

            {body}
        </>
    );
}

/**
 * Displays a content node and recursively displays its children.
 * @params props.content The ContentNode object.
 */
function ContentNode(props) {
    let content = props.content;

    if (Array.isArray(content.children) === false) {
        content.children = [ content.children ];
    }

    return (
        <div>
            {content.source}
            {content.name}
            {content.body}
            <ul>
                {content.children.map((c) => (
                    <li key={c.source}>
                        <ContentNode content={c} />
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default function Home() {
    const [content, setContent] = useState(null);
    
    return (
        <HomeDiv>
            {(content === null && <GetContent setContent={setContent} />) ||
             <ContentNode content={content} />
            }
        </HomeDiv>
    );
}
