// create a small http server using express

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!\n');
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
