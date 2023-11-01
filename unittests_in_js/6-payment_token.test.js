// write a test suite named getPaymentTokenFromAPI
// How to test the result of getPaymentTokenFromAPI(true)?
const chai = require('chai');
const expect = chai.expect;

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should resolve with a successful response when success is true', (done) => {
    // calling the function with success set to true
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // perform assertions using 'expect' from Chai
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
