// Import the required library using ES6 import
import redis from 'redis';

// Create a Redis client instance
const client = redis.createClient(6379, '127.0.0.1');

// Handle Redis client connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
