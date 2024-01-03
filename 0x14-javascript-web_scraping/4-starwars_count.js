#!/usr/bin/node
/**
 * 
 * get specitfy move characters
 *
 */

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results;
      const wedgeAntillesMovies = films.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
      console.log(wedgeAntillesMovies.length);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
