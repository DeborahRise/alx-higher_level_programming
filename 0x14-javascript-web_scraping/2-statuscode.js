#!/usr/bin/node
/**
 * Write a script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */

const request = require('request');

// Check if URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node get_status.js <url>');
  process.exit(1);
}

// Extract URL from command line arguments
const url = process.argv[2];

// Send GET request
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
