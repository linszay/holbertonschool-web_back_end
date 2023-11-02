import kue from 'kue';

// Create a Kue queue lol
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message.',
};

// Create a job and add to queue
const job = queue.create('push_notification_code', jobData);

// Handle job creation success :)
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Handle job completion 100%
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure boooo
job.on('failed', () => {
  console.log('Notification job failed');
});
