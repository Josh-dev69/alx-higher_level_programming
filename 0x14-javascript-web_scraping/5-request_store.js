#!/usr/bin/node
/**
 * Script to get contents of a web page and save it to a file.
 */

const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    // Write data to the file
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.error(err);
      } else {
        console.log(`Data successfully saved to ${filePath}`);
      }
    });
  } else {
    console.error(`Unexpected status code: ${response.statusCode}`);
  }
});

