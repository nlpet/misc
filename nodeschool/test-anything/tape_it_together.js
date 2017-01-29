var test = require('tape');
var fancify = require(process.argv[2]);

 test('fancify', function (t) {
   t.equal(fancify('test'), '~*~test~*~', 'returns a str wrapped in ~*~');
   t.equal(fancify('test', true), '~*~TEST~*~', 'makes the string all caps');
   t.equal(fancify('test', false, '@'), '~@~test~@~', 'allows for changing the character');
   t.end()
 });
