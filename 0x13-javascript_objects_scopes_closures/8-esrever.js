#!/usr/bin/node
// function to return reversed version of a list
exports.esrever = function (list) {
  const newList = [];
  for (let k = list.length - 1; k >= 0; k--) {
    newList.push(list[k]);
  }
  return newList;
};
