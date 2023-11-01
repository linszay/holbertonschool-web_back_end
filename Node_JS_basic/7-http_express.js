// recreate the small http server using Express
const express = require('express');
const { countStudents } = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const studentsData = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\nNumber of students: ${studentsData}`);
  } catch (error) {
    res.send('This is the list of our students\nCannot load the database');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
