#!/usr/bin/node
// It imports an array and computes new array
const list = require('./100-data').list;
console.log(list);
const newList = list.map(function(num, index) {
  return num * index;
});
console.log(newList);
