#!/usr/bin/node
// Write a function that prints the number of arguments
let num = 0;

exports.logMe = function (item) { console.log(`${num++}: ${item}`); };
