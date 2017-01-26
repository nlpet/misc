var R = require('ramda');

var args = R.slice(2, Infinity, process.argv)
var sumOfArgs = R.sum(R.map(parseInt, args))

console.log(sumOfArgs);
