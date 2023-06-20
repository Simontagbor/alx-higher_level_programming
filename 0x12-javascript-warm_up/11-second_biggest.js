#!/usr/bin/node
const args = process.argv;
const arr = Object.values(args).slice(2);
const numbers = arr.map(str => {
  return parseInt(str, 10);
});

function findSecondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  } else {
    return numbers.sort((a, b) => a - b)[numbers.length - 2];
  }
}

console.log(findSecondBiggest(arr));
