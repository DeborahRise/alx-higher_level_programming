#!/usr/bin/node

function factorial(a) {
  if (isNaN(a)) {
    return 1;
  }

  const numA = parseInt(a);
  if (numA <= 1) {
    return 1;
  }

  return numA * factorial(numA - 1);
}

const a = process.argv[2];

if (a === undefined || isNaN(a)) {
  console.log('NaN');
} else {
  console.log(factorial(a));
}
