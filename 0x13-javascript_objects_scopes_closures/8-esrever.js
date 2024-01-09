#!/usr/bin/node
// Write a function that return

exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return (array);
  }, []);
};
