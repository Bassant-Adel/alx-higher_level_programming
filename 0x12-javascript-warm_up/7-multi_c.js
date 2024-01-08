#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let b = 0; b < x; b++) {
    console.log('C is fun');
  }
}
