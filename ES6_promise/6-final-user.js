import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const user = await signUpUser(firstName, lastName);
    const photo = await uploadPhoto(fileName);
    return [
      { status: 'fulfilled', value: user },
      { status: 'rejected', value: photo },
    ];
  } catch (error) {
    return [{ status: 'rejected', value: error.message }];
  }
}
