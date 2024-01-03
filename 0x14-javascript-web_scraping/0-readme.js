#!/usr/bin/node
/**
 *
 * Read and print the content of a file specified in
 * argv[2]
 *
 */
const fs = require('fs');
const filePath = process.argv[2];

// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
