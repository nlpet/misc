'use strict';
/* global first, second */

require('es6-promise');


var firstPromise = first();
var secondPromise = firstPromise.then(function(result) {
  return second(result);
})

secondPromise.then(function(res) {
  console.log(res);
});
