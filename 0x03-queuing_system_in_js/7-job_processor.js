import { createQueue } from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  let totalAttempts = 2;
  let remainingAttempts = 2;
  let timeInterval = setInterval(() => {
    if (totalAttempts - remainingAttempts <= totalAttempts / 2) {
      job.progress(totalAttempts - remainingAttempts, totalAttempts);
    }
    if (blacklist.includes(phoneNumber)) {
      const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
      done(error);
      clearInterval(timeInterval);
      return;
    }
    if (totalAttempts === remainingAttempts) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    --remainingAttempts || done() & clearInterval(timeInterval);
  }, 1000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});