#!/usr/bin/node
/* script to print mynumber: 
 < first arg convert to integer>
 if first arg can be converted to int */
const argv = parseInt(process.argv[2]);
if (Number.isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv);
}
