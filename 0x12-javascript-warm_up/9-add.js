#!/usr/bin/node

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    console.log(parseInt(a) + parseInt(b));
  } else {
    console.log('NaN');
  }
}

const a = process.argv[2];
const b = process.argv[3];

if (a === undefined || b === undefined) {
  console.log('NaN');
} else {
  add(a, b);
}
