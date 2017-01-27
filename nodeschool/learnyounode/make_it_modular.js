var filterFn = require('./readdir_filter');

var dir = process.argv[2]
var ext = process.argv[3]

filterFn(dir, ext, function(err, filenames) {
  if (err) { console.log(err) }
  filenames.forEach(function(file) {
    console.log(file)
  })
})
