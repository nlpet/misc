'use strict';

require('es6-promise');


var promise = new Promise(function (fulfill, reject) {
  setTimeout(() => reject(new Error('REJECTED!')), 300);
});

function onReject (error) {
  console.log(error.message);
}


promise.then(null, (err) => onReject(err));
