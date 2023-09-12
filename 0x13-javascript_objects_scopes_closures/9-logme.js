#!/usr/bin/node
/* function to print number of arguments
already printed and the new argument value */
let k = 0;
exports.logMe = function (item) {
  console.log(k + ': ' + item);
  k++;
};
