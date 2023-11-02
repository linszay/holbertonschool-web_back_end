import kue from 'kue';

// Define an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error if the phone number is blacklisted
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
  } else {
    // Track & update job progress to 50%
    job.progress(50, 100);

    // Log the notification to the console
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
};

// Create a Kue queue lol with a concurrency of 2 jobs at a time
const queue = kue.createQueue({ concurrency: 2 });

// Process jobs in the 'push_notification_code_2' queue
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

