// copying code from task 3 for task 4
// By using sinon.spy, make sure the math used for 
// sendPaymentRequestToApi(100, 20) is the same as 
// Utils.calculateNumber('SUM', 100, 20)
// (validate the usage of the Utils function)
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with correct arguments', () => {
    // creating a spooky spy for Utils.calculateNumber
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    // calling the func
    sendPaymentRequestToApi(100, 20);
    // verifing the spooky spy was called with the correct args
    sinon.assert.calledWithExactly(calculateNumberSpy, 'SUM', 100, 20);
    // restoring the spooky spy after use
    calculateNumberSpy.restore();
  });
});
