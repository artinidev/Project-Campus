const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Database Connection Setup
// Use connection pool for better performance and reconnection
const pool = mysql.createPool({
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || '',
    database: process.env.DB_NAME || 'campus_superia_db',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

const promisePool = pool.promise();

// Basic Health Check Route
app.get('/api/health', async (req, res) => {
    try {
        // Test the database connection
        await promisePool.query('SELECT 1');
        res.json({
            status: 'UP',
            message: 'Backend is running and connected to the database successfully!',
            timestamp: new Date().toISOString()
        });
    } catch (error) {
        console.error('Database connection error:', error);
        res.status(500).json({
            status: 'DOWN',
            message: 'Backend is running but cannot connect to the database.',
            error: error.message
        });
    }
});

// Start Server
app.listen(port, () => {
    console.log(`🚀 Backend API listening on port ${port}`);
});
