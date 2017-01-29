'use strict';

var test = require('tape');
var repeatCallback = require(process.argv[2]);



test('test repeatCallback', function(t) {
  t.plan(3)
  repeatCallback(3, function() {
    t.pass('callback called');
  })
});
