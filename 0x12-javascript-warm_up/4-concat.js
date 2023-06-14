#!/usr/bin/node
if (process.argv[2] === undefined) {
	console.log('undefined is ' + process.argv[2]);
} else if (process.argv[3] === undefined) {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
}
