// The function will take an argument called success (boolean)
// When success is true, it should return a resolved promise 
// with the object {data: 'Successful response from the API' }
// Otherwise, the function is doing nothing.
function getPaymentTokenFromAPI(success) {
    return new Promise((resolve, reject) => {
      if (success) {
        resolve({ data: 'Successful response from the API' });
      } else {
        resolve({});
      }
    });
  }
  
  module.exports = getPaymentTokenFromAPI;
  