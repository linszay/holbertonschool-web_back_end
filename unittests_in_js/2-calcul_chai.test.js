// testing with chai - using expect
const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

const { expect } = chai;

describe('calculateNumber', () => {
  it('should perform the SUM operation correctly', () => {
    expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });

  it('should perform the SUBTRACT operation correctly', () => {
    expect(calculateNumber('SUBTRACT', 1.3, 0)).to.equal(1);
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
  });

  it('should perform the DIVIDE operation correctly', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.equal(0.5);
  });

  it('should throw an error for an invalid type', () => {
    expect(() => calculateNumber('INVALID', 1, 2)).to.throw('Invalid type. Type must be SUM, SUBTRACT, or DIVIDE.');
  });
});

