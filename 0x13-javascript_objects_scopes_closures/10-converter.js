#!/usr/bin/node
// Convert number from base ten to any other
exports.converter = function (base) {
  return function (argv) {
    return argv.toString(base);
  };
};
