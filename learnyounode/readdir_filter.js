var fs = require('fs');
var R = require('ramda');


module.exports = function readdir(dir, ext, callback) {
  fs.readdir(dir, function(err, dirContents) {
    ext = '.' + ext
    if (err) { return callback(err) }
    var filtered =  R.filter(function(f) {
      if (R.slice(-ext.length, Infinity, f) == ext) {
        return f
      }
    }, dirContents)
    return callback(null, filtered)
  })
}
