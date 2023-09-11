#!/usr/bin/node
// Prints first arg passed to it
const argv = process.argv[2];
if (argv === undefined) {
  console.log('No argument');
} else {
  console.log(argv);
}
