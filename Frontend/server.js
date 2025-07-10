const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Sample data
const users = [
  { id: 1, name: 'John Doe', email: 'john@example.com', role: 'admin' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com', role: 'user' },
  { id: 3, name: 'Bob Johnson', email: 'bob@example.com', role: 'user' }
];

const posts = [
  { id: 1, title: 'First Post', content: 'This is the first post content', author: 'John Doe' },
  { id: 2, title: 'Second Post', content: 'This is the second post content', author: 'Jane Smith' },
  { id: 3, title: 'Third Post', content: 'This is the third post content', author: 'Bob Johnson' }
];

// Routes
app.get('/api/hello', (req, res) => {
  res.json({
    message: 'Hello from the backend!',
    timestamp: new Date().toISOString(),
    status: 'success'
  });
});

app.get('/api/users', (req, res) => {
  res.json({
    users: users,
    count: users.length,
    timestamp: new Date().toISOString()
  });
});

app.get('/api/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const user = users.find(u => u.id === userId);
  
  if (!user) {
    return res.status(404).json({
      error: 'User not found',
      message: `No user found with id ${userId}`
    });
  }
  
  res.json({
    user: user,
    timestamp: new Date().toISOString()
  });
});

app.get('/api/posts', (req, res) => {
  res.json({
    posts: posts,
    count: posts.length,
    timestamp: new Date().toISOString()
  });
});

app.get('/api/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const post = posts.find(p => p.id === postId);
  
  if (!post) {
    return res.status(404).json({
      error: 'Post not found',
      message: `No post found with id ${postId}`
    });
  }
  
  res.json({
    post: post,
    timestamp: new Date().toISOString()
  });
});

app.get('/api/status', (req, res) => {
  res.json({
    status: 'running',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: err.message
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    error: 'Route not found',
    message: `The route ${req.originalUrl} does not exist`,
    availableRoutes: [
      'GET /api/hello',
      'GET /api/users',
      'GET /api/users/:id',
      'GET /api/posts',
      'GET /api/posts/:id',
      'GET /api/status'
    ]
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server is running on http://localhost:${PORT}`);
  console.log(`📡 Available endpoints:`);
  console.log(`   GET /api/hello - Basic hello endpoint`);
  console.log(`   GET /api/users - Get all users`);
  console.log(`   GET /api/users/:id - Get user by ID`);
  console.log(`   GET /api/posts - Get all posts`);
  console.log(`   GET /api/posts/:id - Get post by ID`);
  console.log(`   GET /api/status - Server status`);
}); 