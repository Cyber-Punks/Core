![Woman with cybernetic eyes and arms typing in-front of multiple computer screens](./logo.jpg)

# Cyber Punks
Ensure high quality feedback without subjecting moderators to harsh comments.

# Table Of Contents
- [Overview](#overview)

# Overview
A platform which empowers users to receive feedback while maintaining a safe 
space for everyone, without creating an echo chamber of positive comments.

# API Endpoints
http://localhost:8000/sentiment

POST example: 
    {
    "content": "This is a comment. It's not an exact simulation."
    }

Reponse example:
    {
        "naughty": false,
        "subjects": [
            {
                "name": "comment",
                "score": 0.0,
                "magnitude": 0.10000000149011612
            },
            {
                "name": "simulation",
                "score": -0.20000000298023224,
                "magnitude": 0.20000000298023224
            }
        ]
    }
