const express = require('express');
const app = express();
PORT = 27204

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/venues', (req, res) => {
    res.sendFile(__dirname + '/venues.html');
});

app.get('/artists', (req, res) => {
    res.sendFile(__dirname + '/artists.html');
});

app.get('/customers', (req, res) => {
    res.sendFile(__dirname + '/customers.html');
});

app.get('/concerts', (req, res) => {
    res.sendFile(__dirname + '/concerts.html');
});

app.get('/ticketsales', (req, res) => {
    res.sendFile(__dirname + '/ticketsales.html');
});

app.get('/concerts_ticketsales', (req, res) => {
    res.sendFile(__dirname + '/concerts_ticketsales.html');
});

app.listen(PORT, function(){            
    console.log('Express started on http://localhost:' + PORT + '; press Ctrl-C to terminate.')
});