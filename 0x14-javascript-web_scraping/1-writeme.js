#!/usr/bin/node
/**
 * Write a script that writes a string to a file.
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */

const fs = require('fs');

// Check if file path and string to write are provided as arguments
if (process.argv.length < 4) {
  console.error('Usage: node write_file.js <file_path> "<string_to_write>"');
  process.exit(1);
}

// Extract file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write string to file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err); // Print error object if writing fails
  } 
});
