#!/usr/bin/node
// Write a script prints +2 int
function add (a, b) {
  return (a + b);
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
