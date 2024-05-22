#User Authentication && Authorization

This directory is focused on practicing on basices of authentication and authorization. 
-*Here is a detailed prompt about it*

Project Plan:

    Project Setup and Initial Configuration
        How do I install Flask, Flask-JWT-Extended, Redis, and other required dependencies?
        How do I set up a basic Flask project structure?
        How do I configure Flask to use JWT and Redis?

    Basic User Registration and Login
        How do I create a user model for registration and storage (using a simple in-memory list or SQLite for simplicity)?
        How do I implement a user registration endpoint?
        How do I implement a user login endpoint that returns a JWT upon successful authentication?

    JWT Generation and Verification
        How do I set up JWT creation upon successful login?
        How do I implement token verification to protect certain routes?
        How do I create a protected route that is only accessible with a valid JWT?

    Storing JWT in Redis
        How do I set up Redis for storing JWTs?
        How do I implement storing JWTs in Redis with a suitable expiration time?
        How do I modify token verification to check for token validity in Redis?

    Token Revocation and Logout
        How do I implement a logout endpoint that revokes the JWT by removing it from Redis?
        How do I ensure that revoked tokens cannot access protected routes?

    Refresh Tokens
        How do I implement a refresh token mechanism to issue new JWTs without requiring re-authentication?
        How do I store refresh tokens in Redis and manage their lifecycle?

    User Role Management
        How do I add roles to the user model (e.g., admin, user)?
        How do I implement role-based access control (RBAC) for protected routes?
        How do I create protected routes that demonstrate RBAC in action?

    Enhancing Security
        How do I implement additional security measures such as token blacklisting and rate limiting?
        How do I ensure secure storage and transmission of tokens?
        How do I handle common security pitfalls and best practices?

    Testing and Documentation
        How do I write unit tests for all endpoints and functionalities?
        How do I document the API endpoints and usage?
        How do I prepare a guide on setting up and running the project?

    Deployment
        How do I prepare the project for deployment?
        How do I deploy the project to a cloud platform (e.g., Heroku, AWS)?
        How do I ensure the project is secure and scalable in a production environment?
