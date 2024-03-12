#!/usr/bin/node

const args = process.argv;

if (!isNaN(args[2])) {
  const size = parseInt(args[2]);

  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
