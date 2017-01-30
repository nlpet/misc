'use strict';

var chai = require('chai');
var expect = chai.expect;
var sinon = require('sinon');

var CartSummary = require('./cart-summary.js');
var tax = require('./tax.js');


describe('CartSummary', function() {
  it('getSubtotal() should reutnr 0 if no items are passed in', function() {
    var cartSummary = new CartSummary([]);
    expect(cartSummary.getSubtotal()).to.equal(0);
  });

  it('getSubtotal() should return the sum of the price * quantity for all items', function () {
    var cartSummary = new CartSummary([{
      id: 101,
      quantity: 5,
      price: 35
    }, {
      id: 102,
      quantity: 1,
      price: 25
    }, {
      id: 103,
      quantity: 10,
      price: 11
    }]);

    expect(cartSummary.getSubtotal()).to.equal(310);
  })
});


describe('getTax()', function() {
  beforeEach(function() {
    sinon.stub(tax, 'calculate', function(subtotal, state, done) {
      setTimeout(function() {
        done({
          amount: 50
        });
      }, 0);
    });
  });

  afterEach(function() {
    tax.calculate.restore();
  });

  it('get Tax() should execute the callback function with the tax amount', function(done) {
    var cartSummary = new CartSummary([{
      id: 101,
      quantity: 5,
      price: 35
    }, {
      id: 102,
      quantity: 1,
      price: 25
    }, {
      id: 103,
      quantity: 10,
      price: 11
    }]);

    cartSummary.getTax('LN', function(taxAmount) {
      expect(taxAmount).to.equal(50);
      done();
    });
  });

  it('getTax() should execute the callback function with the tax amount', function(done) {
    var cartSummary = new CartSummary([{
      id: 101,
      quantity: 5,
      price: 35
    }, {
      id: 102,
      quantity: 1,
      price: 25
    }, {
      id: 103,
      quantity: 10,
      price: 11
    }]);

    cartSummary.getTax('LN', function(taxAmount) {
      expect(taxAmount).to.equal(50);
      expect(tax.calculate.getCall(0).args[0]).to.equal(310);
      expect(tax.calculate.getCall(0).args[1]).to.equal('LN');
      done();
    });
  });
});
