// Create one suite for the index page:
// Correct status code?
// Correct result?
// Other?
const request = require('request');
const { expect } = require('chai');
const app = require('./api');

const baseUrl = 'http://localhost:7865';

describe('Index page', () => {
  before(function (done) {
    app.listen(7865, function () {
      done();
    });
  });

  it('should return correct status code', (done) => {
    request.get(`${baseUrl}`, (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result', (done) => {
    request.get(`${baseUrl}`, (err, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should not return an error message', (done) => {
    request.get(`${baseUrl}`, (err, response, body) => {
      expect(body).to.not.include('Error');
      done();
    });
  });
});
