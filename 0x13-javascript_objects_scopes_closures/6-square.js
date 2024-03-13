#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < Number(this.height); i++) {
      let toPrint = '';
      for (let j = 0; j < Number(this.width); j++) {
        toPrint += 'X';
      }
      console.log(toPrint);
    }
  }

  rotate () {
    const temp = Number(this.height);
    this.height = Number(this.width);
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    super.print();
  }

  double () {
    super.double();
  }
}

class Square2 extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
    // toPrint += c;
  }
}

module.exports = Square2;
