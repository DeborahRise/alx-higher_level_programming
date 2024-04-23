#!/usr/bin/node
/**
 * Write a script that reads and prints the content of a file.
 * The first argument is the file path
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */


fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data); // File content
  });
