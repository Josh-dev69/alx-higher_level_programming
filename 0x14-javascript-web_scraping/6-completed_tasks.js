#!/usr/bin/node
/**
 * Script to compute the number of completed tasks by user id.
 */

const request = require('request');

const apiUrl = process.argv[2];

const(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Count completed tasks for each user
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Unexpected status code: ${response.statusCode}`);
  }
});
