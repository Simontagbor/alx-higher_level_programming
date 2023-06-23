#!/usr/bin/node

exports.addMeMaybe = function (num, func) {
  num += 1;
  return func(num);
};
