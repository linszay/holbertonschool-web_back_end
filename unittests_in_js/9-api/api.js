// By using express, create an instance of express called app
// Listen to port 7865 and log API available on localhost port 7865
// to the browser console when the express server is started
// For the route GET /, return the msg Welcome to the payment system
const express = require('express');
const app = express();
const port = 7865;

// validate :id as a number
app.param('id', (req, res, next, id) => {
  if (isNaN(id)) {
    // if :id is not a number, return a 404 response
    res.status(404).send('Not Found');
  } else {
    // if :id is a number, continue to the next middleware
    next();
  }
});

// new endpoint for /cart/:id
app.get('/cart/:id', (req, res) => {
  // this is reached if :id is a number
  const cartId = req.params.id;
  res.status(200).send(`Payment methods for cart ${cartId}`);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
