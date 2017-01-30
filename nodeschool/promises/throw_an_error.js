'use strict';
/* global first, second */

require('es6-promise');
var q = require('q');

var invalidJSON = process.argv[2];


function parsePromised(json) {
  return new Promise(function (fulfill, reject) {
    try {
      fulfill(JSON.parse(json));
    } catch (e) {
      reject(e);
    }
  });
}


parsePromised(invalidJSON)
  .then(null, console.log)
