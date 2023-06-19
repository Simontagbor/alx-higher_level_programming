#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args);
const a = parseInt(arr[2]);
const b = parseInt(arr[3]);

function add (a, b) {
  console.log(a + b);
}
add(a, b);
