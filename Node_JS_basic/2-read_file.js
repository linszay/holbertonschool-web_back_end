// func accepts path in arg
// attempts to read db file async
// throws error if if db unavailable
// otherwise logs message to console

const fs = require('fs');

function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf-8');
    const lines = data.split('\n');

    let totalStudents = 0;
    const fieldCount = {};
    const fieldNames = {};

    for (const line of lines) {
      const [firstName, field] = line.split(',');
      if (firstName && field) {
        totalStudents++;
        if (!fieldCount[field]) {
          fieldCount[field] = 1;
          fieldNames[field] = [firstName];
        } else {
          fieldCount[field]++;
          fieldNames[field].push(firstName);
        }
      }
    }

    console.log(`Number of students: ${totalStudents}`);
    for (const field in fieldCount) {
      console.log(`Number of students in ${field}: ${fieldCount[field]}. List: ${fieldNames[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
