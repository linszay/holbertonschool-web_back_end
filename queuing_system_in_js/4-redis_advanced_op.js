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

// Create Hash using hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display Hash using hgetall
client.hgetall('HolbertonSchools', (error, reply) => {
  if (error) {
    console.error(error);
  } else {
    console.log(reply);
  }
});

