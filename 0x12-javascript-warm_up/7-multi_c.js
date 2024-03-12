#!/usr/bin/node

const args = process.argv;

if (!isNaN(args[2])) {
  while (args[2] > 0) {
    console.log('C is fun');
    args[2] -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}
