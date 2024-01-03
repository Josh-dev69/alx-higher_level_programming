#!/usr/bin/node
/**
 * Script to print all characters of a Star Wars movie.
 */

const request = require('request');

const movieID = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);

    movie.characters.forEach(characterUrl => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.error(`Unexpected status code for character: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Unexpected status code: ${response.statusCode}`);
  }
});

