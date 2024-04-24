#!/usr/bin/node
/**
 * Write a script that computes the number of tasks completed by user id.
 */

const request = require('request');

// Check if API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node completed_tasks.js <api_url>');
  process.exit(1);
}

// Extract API URL from command line arguments
const apiUrl = process.argv[2];

// Send GET request to the JSONPlaceholder API to fetch todos
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      // Iterate over todos to count completed tasks for each user
      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      // Print users with completed tasks
      console.log('{');
      Object.keys(completedTasksByUser).forEach((userId, index, array) => {
        console.log(`  '${userId}': ${completedTasksByUser[userId]}${index === array.length - 1 ? '' : ','}`);
      });
      console.log('}');
    }
  }
});
