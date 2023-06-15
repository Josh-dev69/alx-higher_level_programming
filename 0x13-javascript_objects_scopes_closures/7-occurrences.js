#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrence = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurrence++;
    }
  }
  return occurrence;
};
