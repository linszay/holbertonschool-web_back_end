/* eslint-disable no-unused-vars */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((responses) => {
      const [photoResponse, userResponse] = responses;
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch((error) => {
      console.log('Signup system offline');
    });
}
