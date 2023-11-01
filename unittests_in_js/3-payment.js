// func calls utils.calculateNumber with type SUM, totalAmount as a, 
// totalShipping as b and display in the console the message 
// The total is: <result of the sum>
const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;
