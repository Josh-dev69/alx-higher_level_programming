#!/usr/bin/node
exports.callMeMoby = function (num, newFunct) {
  for (let i = 0; i < num; i++) {
    newFunct();
  }
};
