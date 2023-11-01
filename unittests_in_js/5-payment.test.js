// Inside the same describe, create 2 tests:
// The first test will call sendPaymentRequestToAPI with 100, and 20:
// Verify that the console is logging the string The total is: 120
// Verify that the console is only called once
// The second test will call sendPaymentRequestToAPI with 10, and 10:
// Verify that the console is logging the string The total is: 20
// Verify that the console is only called once
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;
  beforeEach(() => {
    // create a spy for console.log before each test
    consoleLogSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    // restore the spooky spy after each test
    consoleLogSpy.restore();
  });
  it('should log the total for 100 and 20 and only call console.log once', () => {
    // call func with the first test values
    sendPaymentRequestToApi(100, 20);
    // verify console.log is logging the correct message
    sinon.assert.calledWithExactly(consoleLogSpy, 'The total is: 120');
    // verify console.log is only called once
    sinon.assert.calledOnce(consoleLogSpy);
  });
  it('should log the total for 10 and 10 and only call console.log once', () => {
    // call func with the second test values
    sendPaymentRequestToApi(10, 10);
    // verify console.log is logging the correct message
    sinon.assert.calledWithExactly(consoleLogSpy, 'The total is: 20');
    // verify console.log is only called once
    sinon.assert.calledOnce(consoleLogSpy);
  });
});
