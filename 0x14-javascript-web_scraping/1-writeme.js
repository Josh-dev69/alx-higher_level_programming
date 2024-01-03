#!/usr/bin/node
/**
 *
 * Write to a file via the content of a command line
 * argument
 *
*/ 
const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

