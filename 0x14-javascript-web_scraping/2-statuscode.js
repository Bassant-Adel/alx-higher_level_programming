#!/usr/bin/node
// The first argument is the URL to request (GET)

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (!error) console.log('code:', response.statusCode);
});
