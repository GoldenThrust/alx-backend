import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

const jobData = [
  {
    phoneNumber: '2153818780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '7153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '8153518743',
    message: 'This is the code 4321 to verify your account'
  }
]

describe('createPushNotificationsJobs', () => {
  const log = sinon.spy(console, 'log');
  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
    log.resetHistory();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display error', () => {
    expect(() => createPushNotificationsJobs("hello", queue)).to.throw('Jobs is not an array');
  });

  it('should display', (done) => {
    expect(queue.testMode.jobs.length).to.equal(0);
    createPushNotificationsJobs(jobData, queue);
    expect(queue.testMode.jobs.length).to.equal(3);
    done()
  })
})