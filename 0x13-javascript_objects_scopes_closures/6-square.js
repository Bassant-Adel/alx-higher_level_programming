#!/usr/bin/node
// You must use the class notation

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let b = 0; b < this.height; b++) console.log(c.repeat(this.width));
    }
  }
};
