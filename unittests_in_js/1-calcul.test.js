const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  it('should round and add two numbers when type is SUM', function () {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('should round and subtract b from a when type is SUBTRACT', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });

  it('should round and divide a by b when type is DIVIDE', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

  it('should return "Error" when dividing by 0', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });

  it('should throw an error for an invalid type', function () {
    assert.throws(() => calculateNumber('INVALID_TYPE', 1.4, 4.5), {
      name: 'Error',
      message: 'Invalid type. Type must be SUM, SUBTRACT, or DIVIDE.',
    });
  });
});
