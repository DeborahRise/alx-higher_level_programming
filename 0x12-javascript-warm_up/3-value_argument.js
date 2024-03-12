#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('No Argument');
} else {
  console.log(args[2]);
}
