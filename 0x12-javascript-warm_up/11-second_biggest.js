#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args).slice(2);

function findSecondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  } else {
    return parseInt(arr.sort()[arr.length - 2]);
  }
}

console.log(findSecondBiggest(arr));
