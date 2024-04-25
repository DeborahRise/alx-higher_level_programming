#!/usr/bin/node
/**
 * Write a script that computes the number of tasks completed by user id.
 */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const tasks = JSON.parse(body);
  const completed = {};
  for (const task of tasks) {
    if (task.completed) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
