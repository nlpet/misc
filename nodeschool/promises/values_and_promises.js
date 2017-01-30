'use strict';
/* global first, second */

require('es6-promise');


function attachTitle (fs) {
  return `DR. ${fs}`;
}

var promise = Promise.resolve('MANHATTAN');

promise
  .then(attachTitle)
  .then(console.log);
