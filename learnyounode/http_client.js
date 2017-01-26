var http = require('http')
var R = require('ramda');

var url = process.argv[2]

if (url && R.contains('http', url)) {
  http.get(url, function(req) {
    req.setEncoding('utf-8')
    req.on('data', console.log)
    req.on('error', console.error)
  }).on('error', console.error)
} else {
  console.log('Error: not a valid url')
}
