// stub utils.calculateNumber to always return 10
// verify the stub is called with type = SUM, a = 100, and b = 20
// add a spy to verify that console.log is logging 
// the correct message The total is: 10
const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;
