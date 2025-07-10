# Backend Server

A simple Express.js backend server that provides API endpoints for the React frontend.

## Features

- RESTful API endpoints
- CORS enabled for frontend communication
- Sample data (users and posts)
- Error handling
- Status endpoint

## Available Endpoints

- `GET /api/hello` - Basic hello endpoint
- `GET /api/users` - Get all users
- `GET /api/users/:id` - Get user by ID
- `GET /api/posts` - Get all posts
- `GET /api/posts/:id` - Get post by ID
- `GET /api/status` - Server status

## Installation

```bash
npm install
```

## Running the Server

```bash
npm start
```

The server will start on `http://localhost:3000`

## Development

```bash
npm run dev
```

## Sample Data

The server includes sample data for testing:

### Users
- John Doe (admin)
- Jane Smith (user)
- Bob Johnson (user)

### Posts
- First Post (by John Doe)
- Second Post (by Jane Smith)
- Third Post (by Bob Johnson)
