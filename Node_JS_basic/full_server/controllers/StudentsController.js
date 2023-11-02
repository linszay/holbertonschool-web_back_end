// student controller
const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(req.app.locals.database);
      res.status(200).send(`This is the list of our students\n${formatStudents(students)}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase(req.app.locals.database);
      const majorStudents = students[major] || [];
      res.status(200).send(`List: ${majorStudents.join(', ')}\n`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

function formatStudents(students) {
  const fields = Object.keys(students).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
  const result = [];
  fields.forEach(field => {
    result.push(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
  });
  return result.join('\n');
}

module.exports = StudentsController;
