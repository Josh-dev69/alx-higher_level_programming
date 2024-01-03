#!/usr/bin/node
/**
 * script the get the title of movies
 *
 */
const request = require('request');

const movieid = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  if (response.statusCode === 200) {
    console.log(data.title);
  }
});
