#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args);
const num = parseInt(arr[2]);

function factorial (num) {
  if (num >= 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
console.log(factorial(num));
