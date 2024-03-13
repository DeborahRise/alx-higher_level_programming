#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let i = 1;
  while (i <= x) {
    theFunction();
    i++;
  }
}

module.exports = { callMeMoby };
