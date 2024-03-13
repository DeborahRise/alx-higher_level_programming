#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < Number(this.height); i++) {
      let toPrint = '';
      for (let j = 0; j < Number(this.width); j++) {
        toPrint += c;
      }
      console.log(toPrint);
    }
  }
};
