#!/usr/bin/node
// function to return number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (let k = 0; k < list.length; k++) {
    if (list[k] === searchElement) {
      times += 1;
    }
  }
  return times;
};
