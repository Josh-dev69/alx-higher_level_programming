#!/usr/bin/node
/**
 * Write to a file via the content of a command line
 * argument
 *
 */ 
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

