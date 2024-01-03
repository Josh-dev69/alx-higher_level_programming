#!/usr/bin/node
/**
 * script to get contents of web and save in a file
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

function getData (url, callback) {
  request(url, function (error, response, body) {
    if (error) {
      callback(error);
      return;
    }
    if (response.statusCode === 200) {
      callback(null, body);
    }
  });
}

getData(url, function (error, body) {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
