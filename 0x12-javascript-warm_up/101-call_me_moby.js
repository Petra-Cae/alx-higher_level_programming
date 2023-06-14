#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let mb = 0; mb < x; mb++) theFunction();
};
