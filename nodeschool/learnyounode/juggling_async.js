

var http = require('http')
var R = require('ramda');

var url = process.argv[2]


var res = ''
http.get(url, function(req) {
  req.setEncoding('utf-8')
  req.on('data', function(data) {
    res += data
  })
  req.on('end', function(data) {
    console.log(res.length)
    console.log(res)
  })
  req.on('error', console.error)
}).on('error', console.error)
