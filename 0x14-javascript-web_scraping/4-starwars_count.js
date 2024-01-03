#!/usr/bin/node
/**
 * Get movies with the character "Wedge Antilles" (character ID 18).
 */

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    // Filter movies based on the presence of the character "Wedge Antilles" (character ID 18)
    const wedgeAntillesMovies = films.filter(movie =>
      movie.characters.some(character =>
        character.endsWith('/18/')
      )
    );
    console.log(wedgeAntillesMovies.length);
  } else {
    console.error(`Unexpected status code: ${response.statusCode}`);
  }
});
