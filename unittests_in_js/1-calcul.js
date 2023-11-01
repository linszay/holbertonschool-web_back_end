// updating 0-calcul with new arg type which can be sum, subtract, or divide
// updated for testing
function calculateNumber(type, a, b) {
    if (type === 'SUM') {
      return Math.round(a) + Math.round(b);
    } else if (type === 'SUBTRACT') {
      return Math.round(a) - Math.round(b);
    } else if (type === 'DIVIDE') {
      const roundedB = Math.round(b);
      if (roundedB === 0) {
        return 'Error';
      }
      return Math.round(a) / roundedB;
    } else {
      throw new Error('Invalid type. Type must be SUM, SUBTRACT, or DIVIDE.');
    }
  }
  
  module.exports = calculateNumber;
  