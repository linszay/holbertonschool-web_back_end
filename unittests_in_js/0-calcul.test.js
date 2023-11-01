// test cases for 0-calcul
// updated for testing

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should round two numbers and return their sum', () => {
    assert.strictEqual(calculateNumber(1.3, 0), 1);
  });

  it('should round two numbers and return their sum', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round two numbers and return their sum', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round two numbers and return their sum', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
