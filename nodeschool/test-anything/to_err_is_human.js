'use strict';

var test = require('tape');
var feedCat = require(process.argv[2]);


test('test repeatCallback', function(t) {
  t.equal(feedCat('biscuits'), 'yum', 'feed the cat some biscuits');
  t.equal(feedCat('water'), 'yum', 'give the cat some water');
  t.equal(feedCat('wet food'), 'yum', 'feed the cat some wet food');
  t.throws(feedCat.bind(null, 'chocolate'));
  t.end();
});
