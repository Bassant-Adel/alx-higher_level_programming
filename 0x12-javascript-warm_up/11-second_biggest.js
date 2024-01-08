#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const row = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((n, b) => (n - b));
  console.log(row[row.length - 2]);
}
