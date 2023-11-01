// Create one suite for the index page:
// Correct status code?
// Correct result?
// Other?
const { expect } = require('chai');
const request = require('request');

const apiUrl = 'http://localhost:7865';

describe('Cart page', () => {
  it('returns Payment methods for cart when :id is a number', (done) => {
    request(`${apiUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns 404 when :id is NOT a number', (done) => {
    request(`${apiUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
