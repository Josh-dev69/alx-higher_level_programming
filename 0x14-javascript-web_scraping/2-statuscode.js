#!/usr/bin/node
/**
 *
 * A Script that prompts the status code of a GET
 * request
 *
*/
const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
