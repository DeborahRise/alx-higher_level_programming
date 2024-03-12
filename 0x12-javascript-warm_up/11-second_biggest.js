#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let largeNum = 0;
  let secNum = 0;

  for (let i = 2; i < args.length; i++) {
    const currentNum = Number(args[i]);
    if (currentNum > largeNum) {
      secNum = largeNum;
      largeNum = currentNum;
    } else if (currentNum > secNum && currentNum < largeNum) {
      secNum = currentNum;
    }
  }
  console.log(secNum);
}
