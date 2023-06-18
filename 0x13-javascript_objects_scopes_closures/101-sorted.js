#!/usr/bin/node

/**
A script that imports a dictionary of occurrences by user id 
and computes a dictionary of user ids by occurrence
*/

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
