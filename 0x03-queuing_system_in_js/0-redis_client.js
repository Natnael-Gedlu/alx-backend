#!/usr/bin/yarn dev

// Importing the required module
import { createClient } from 'redis';

// Creating a Redis client
const client = createClient();

// Event handler for errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
