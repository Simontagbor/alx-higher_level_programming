#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args);
const str = 'C is fun';

if (isNaN(parseInt(arr[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arr[2]; i++) {
    console.log(str);
  }
}
