var fs = require('fs');
var R = require('ramda');

var dir = process.argv[2]
var ext = '.' + process.argv[3]


fs.readdir(dir, function(err, dirContents) {
  if (err) { return console.log(err) }
    R.map(function(f) {
      if (R.slice(-ext.length, Infinity, f) == ext) {
        console.log(f)
      }
    }, dirContents)
})
