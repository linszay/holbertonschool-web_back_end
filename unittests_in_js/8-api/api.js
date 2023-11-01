// By using express, create an instance of express called app
// Listen to port 7865 and log API available on localhost port 7865
// to the browser console when the express server is started
// For the route GET /, return the msg Welcome to the payment system
const express = require('express');
const app = express();

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

module.exports = app;
