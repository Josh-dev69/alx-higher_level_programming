#!/usr/bin/node
function factorialFinder(num) {
  if (num === 0) {
    return (1);
  } else {
    return (factorialFinder(num - 1) * num);
  }
}
const num = parseInt(process.argv[2]);
if (num) {
  console.log(factorialFinder(num));
} else {
  console.log(1);
}
