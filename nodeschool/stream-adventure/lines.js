/*

Instead of transforming every line as in the previous "TRANSFORM" example,
for this challenge, convert even-numbered lines to upper-case and odd-numbered
lines to lower-case. Consider the first line to be odd-numbered. For example
given this input:

    One
    Two
    Three
    Four

Your program should output:

    one
    TWO
    three
    FOUR

You can use the `split` module to split input by newlines. For example:

    var split = require('split');
    process.stdin
        .pipe(split())
        .pipe(through2(function (line, _, next) {
            console.dir(line.toString());
            next();
        }))
    ;

`split` will buffer chunks on newlines before you get them. In the previous
example, we will get separate events for each line even though all the data
probably arrives on the same chunk:

    $ echo -e 'one\ntwo\nthree' | node split.js
    'one'
    'two'
    'three'

Your own program should use `split` in this way, but you should transform the
input and pipe the output through to `process.stdout`.

*/

var through = require('through2');
var split = require('split');

var counter = 0;

var transform = through(function (buffer, _, next) {
  var line = buffer.toString();
  this.push(counter % 2 === 0
      ? line.toLowerCase() + '\n'
      : line.toUpperCase() + '\n'
  );
  counter ++;
  next();
});

process.stdin
  .pipe(split())
  .pipe(transform)
  .pipe(process.stdout);
