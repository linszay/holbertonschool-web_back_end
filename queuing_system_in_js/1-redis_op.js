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

// Function sets a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function isplays the value of a school
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.error(error);
    } else {
      console.log(reply);
    }
  });
};

// Call the functionssss
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
