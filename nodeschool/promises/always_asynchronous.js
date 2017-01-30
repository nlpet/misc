'use strict';

require('es6-promise');

var promise = new Promise(function (fulfill, reject) {
  fulfill('PROMISE VALUE');
});


promise.then(console.log, null);

console.log('MAIN PROGRAM');
