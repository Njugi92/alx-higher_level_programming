#!/usr/bin/node
// Script to print a square
const size = process.argv[2];
if (isNaN(size)) {
	console.log('Missing size');
}else {
	for (let k = 0; k < size; k++) {
		console.log('X'.repeat(size));
	}
}
