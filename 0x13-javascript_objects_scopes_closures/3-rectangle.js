#!/usr/bin/node
// You must use the class notation

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
  print () {
    for (let b = 0; b < this.height; b++) console.log('X'.repeat(this.width));
  }
};
