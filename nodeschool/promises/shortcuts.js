'use strict';

require('es6-promise');


var promise = Promise.reject(new Error('FATAL ERR0R'));

promise.catch((err) => console.error(err.message));
