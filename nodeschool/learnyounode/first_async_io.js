var fs = require('fs');

var contents = fs.readFile(process.argv[2], function doneReading(err, contents) {
  if (err) { return console.log('Error:', err) }
  var lines = contents.toString().split('\n').length - 1
  console.log(lines)
})
