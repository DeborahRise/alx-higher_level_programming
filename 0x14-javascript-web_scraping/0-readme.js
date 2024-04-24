#!/usr/bin/node
/**
 * Write a script that reads and prints the content of a file.
 * The first argument is the file path
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */

const fs = require('fs');

// Check if file path is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

// Extract file path from command line arguments
const filePath = process.argv[2];

// Read file content
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err); // Print error object if reading fails
  } else {
    console.log(data); // Print file content if reading succeeds
  }
});
