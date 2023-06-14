#!/usr/bin/node
const arg = process.argv;
if (arg.length < 4) {
  console.log(0);
} else {
  const argArray = arg.slice(2).sort((a, b) => a - b).reverse();
  console.log(argArray[1]);
}
