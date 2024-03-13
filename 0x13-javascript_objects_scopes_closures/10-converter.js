#!/usr/bin/node

let countArgs = 0;

exports.logMe = function (item) {
  console.log(`${countArgs}: ${item}`);
  countArgs++;
};
