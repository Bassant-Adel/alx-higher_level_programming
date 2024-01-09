#!/usr/bin/node
// You must use the class notationing your class

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
