import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const redisClient = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const initialSeats = 50;
let reservationEnabled = true;
const PORT = 1245;

async function reserveSeat(number) {
  const setAsync = promisify(redisClient.SET).bind(redisClient);

  try {
    const response = await setAsync('available_seats', number);
    return response;
  } catch (err) {
    return err;
  }
};


async function getCurrentAvailableSeats() {
  const getAsync = promisify(redisClient.GET).bind(redisClient);

  try {
    const response = await getAsync('available_seats');
    return response;
  } catch (err) {
    return err;
  }
};

app.get('/available_seats', (req, res) => {
  getCurrentAvailableSeats()
    .then((numberOfAvailableSeats) => {
      res.json({ numberOfAvailableSeats })
    });
});

app.get('/reserve_seat', (_req, res) => {
  if (reservationEnabled) {
    try {
      const job = queue.create('reserve_seat');

      job.on('complete', () => {
        console.log(
          'Seat reservation job',
          job.id,
          'completed'
        );
      });

      job.on('failed', (err) => {
        console.log(
          'Seat reservation job',
          job.id,
          'failed:',
          err.message || err.toString(),
        );
      });

      job.save();
      res.json({ status: 'Reservation in process' });
    } catch {
      res.json({ status: 'Reservation failed' });
    }
  } else {
    res.json({ status: 'Reservation are blocked' });
  }
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', (job, done) => {
    getCurrentAvailableSeats()
      .then((availableSeats) => {
        availableSeats = Number(availableSeats || 0)
        reservationEnabled = availableSeats <= 1 ? false : true;
        if (availableSeats >= 1) {
          reserveSeat(availableSeats - 1)
            .then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
      });
  });
});


app.listen(PORT, () => {
  reserveSeat(initialSeats)
});

export default app;