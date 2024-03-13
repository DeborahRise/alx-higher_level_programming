#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;

  for (let element of list) {
    if (element === searchElement) {
      num++;
	}
  }
  return num;
}
