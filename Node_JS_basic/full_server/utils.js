// utils file
const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (error, data) => {
      if (error) {
        reject(error);
      } else {
        const lines = data.split('\n').filter(line => line.trim() !== '');

        const students = {};
        lines.forEach(line => {
          const [firstName, field] = line.split(',');
          if (field === 'CS' || field === 'SWE') {
            if (!students[field]) {
              students[field] = [firstName];
            } else {
              students[field].push(firstName);
            }
          }
        });

        resolve(students);
      }
    });
  });
}

module.exports = {
  readDatabase,
};
