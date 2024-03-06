import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});


async function setNewSchool(schoolName, value) {
    await client.SET(schoolName, value, print);
}


async function displaySchoolValue(schoolName) {
    await client.GET(schoolName, (_err, res) => console.log(res))
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');