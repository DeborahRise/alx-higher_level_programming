#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  let i = 1;
  while (i <= number) {
    theFunction(i);
    i++;
  }
}

module.exports = { addMeMaybe };
