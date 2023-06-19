#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args);
const str = 'x';

if (isNaN(parseInt(arr[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arr[2]; i++) {
    console.log(str.repeat(arr[2]));
  }
}
