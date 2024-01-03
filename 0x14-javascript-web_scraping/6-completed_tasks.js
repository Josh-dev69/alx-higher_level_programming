#!/usr/bin/node
/**
 * Script to compute the number of completed tasks by user id.
 */

const request = require('request');
const apiUrl = process.argv[2]
request(apiUrl, function (err, _res, body) {
  if (err) {
    console.error(err);
  } else {
    try {
      const completedTasksByUsers = {};
      body = JSON.parse(body);

      for (let i = 0; i < body.length; ++i) {
        const userId = body[i].userId;
        const completed = body[i].completed;

        if (completed && !completedTasksByUsers[userId]) {
          completedTasksByUsers[userId] = 0;
        }

        if (completed) ++completedTasksByUsers[userId];
      }

      console.log(completedTasksByUsers);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
