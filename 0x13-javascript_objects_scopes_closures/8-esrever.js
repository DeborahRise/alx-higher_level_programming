#!/usr/bin/node

exports.esrever = function (list) {
  let y = list.length;
  let newList = [];
  for (let x = 0; y > 0; x++) {
    newList.push(list[y-1]);
    y -= 1;
  }
  return newList;
}
