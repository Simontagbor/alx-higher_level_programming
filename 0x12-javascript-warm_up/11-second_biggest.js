#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args).slice(2);

function findSecondBiggest (arr) {
  if (arr.length <= 3) {
    return 0;
  } else {
    return arr.sort()[arr.length - 2];
  }
}

console.log(findSecondBiggest(arr));
