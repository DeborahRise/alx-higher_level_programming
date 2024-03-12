#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let largeNum = 0;
  let secNum = 0;

  for (let i = 2; i < args.length; i++) {
    if (args[i] > largeNum) {
      secNum = largeNum;
      largeNum = args[i];
    }
  }
  console.log(secNum);
}
