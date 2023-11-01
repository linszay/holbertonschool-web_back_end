// new func takes a path arg
// attempts to read the db file async
// should return a promise
const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n');
        const fieldCount = {};
        const fieldNames = {};

        for (const line of lines) {
          const [firstName, field] = line.split(',');
          if (firstName && field) {
            if (!fieldCount[field]) {
              fieldCount[field] = 1;
              fieldNames[field] = [firstName];
            } else {
              fieldCount[field] += 1;
              fieldNames[field].push(firstName);
            }
          }
        }

        console.log(`Number of students: ${lines.length - 1}`);
        for (const field in fieldCount) {
          if (Object.prototype.hasOwnProperty.call(fieldCount, field)) {
            console.log(`Number of students in ${field}: ${fieldCount[field]}. List: ${fieldNames[field].join(', ')}`);
          }
        }

        resolve();
      }
    });
  });
}

module.exports = countStudents;
