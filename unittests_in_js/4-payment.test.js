// Stub Utils.calculateNumber to always return the same number 10
// Verify the stub is called with type = SUM, a = 100, and b = 20
// Add a spy to verify console.log is logging the correct message
// The total is: 10
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with type SUM and display the correct message', () => {
    // creating a stub for Utils.calculateNumber
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // creating a spooky spy for console.log
    const consoleLogSpy = sinon.spy(console, 'log');
    // calling the func
    sendPaymentRequestToApi(100, 20);
    // verifying the stub was called with correct args
    sinon.assert.calledWithExactly(calculateNumberStub, 'SUM', 100, 20);
    // verifying console.log is logging the correct message
    sinon.assert.calledWithExactly(consoleLogSpy, 'The total is: 10');
    // restore the stub and spy after use
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });
});
