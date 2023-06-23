#!/usr/bin/node

exports.callMeMoby = function (num, func) {
  for (let i = 1; i <= num; i++) {
    func();
  }
};
