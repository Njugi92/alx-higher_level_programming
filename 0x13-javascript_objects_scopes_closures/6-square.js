#!/usr/bin/node
// class Square that defines square & inherits from Square 5-square.js
const Squa = require('./5-square.js');
class Square extends Squa {
  charPrint (c) {
    for (let k = 0; k < this.width; k++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
