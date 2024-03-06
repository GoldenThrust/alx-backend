import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});


const hashName = 'HolbertonSchools'
const schoolLoc = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
};

function hashSetCache(name, key, value) {
    client.HSET(name, key, value, print)
}

function printHashSet(name) {
    client.HGETALL(name, (_err, resp) => console.log(resp))
}

function cacheObject(hashName, Obj) {
    for (const [key, value] of Object.entries(Obj)) {
        hashSetCache(hashName, key, value);
    }

    printHashSet(hashName)
}

client.on('connect', () => {
    cacheObject(hashName, schoolLoc)
    console.log('Redis client connected to the server');
});

