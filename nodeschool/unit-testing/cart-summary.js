'use strict';
var tax = require('./tax.js');

function CartSummary(items) {
  this._items = items;
}

CartSummary.prototype.getSubtotal = function() {
  if (this._items.length) {
    return this._items.reduce(function(subtotal, items) {
      return subtotal += (items.quantity * items.price);
    }, 0);
  }
  return 0;
}

CartSummary.prototype.getTax = function(state, done) {
  tax.calculate(this.getSubtotal(), state, function(taxInfo) {
    done(taxInfo.amount);
  });
};

module.exports = CartSummary;
