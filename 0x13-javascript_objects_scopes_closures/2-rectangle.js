#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      const Rectangle = {};

      /*  if (Number(w) <= 0 || Number(h) <= 0) {
    let Rectangle = new object(); */
    }
  }
}

module.exports = Rectangle;
