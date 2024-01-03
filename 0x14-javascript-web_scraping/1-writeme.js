#!/usr/bin/node
/**
 *
 * Write to a file via the content of a command line
 * argument
 *
*/ 
const fs = require('fs');

// Extract the file path and content from command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});

