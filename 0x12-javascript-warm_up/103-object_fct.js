#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

Object.assign(myObject, {
  incr: function () {
    this.value++;
  }
});

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
