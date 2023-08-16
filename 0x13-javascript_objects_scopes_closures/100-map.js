#!/usr/bin/node

/**
A script that imports an array and computes a new array
*/

const arr = require('./100-data').list;

console.log(arr);
console.log(arr.map((x, idx) => x * idx));
