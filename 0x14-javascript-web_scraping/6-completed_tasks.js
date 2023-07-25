#!/usr/bin/node
/*
Computes the number of tasks completed by a user ID
*/

const req = require('request');
const url = process.argv[2];
const completedTasks = {};

req.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
