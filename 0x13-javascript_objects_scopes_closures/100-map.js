#!/usr/bin/node
// Write a script that imports an array

const list = require('./100-data.js').list;
console.log(list);

console.log(list.map((item, index) => item * index));
