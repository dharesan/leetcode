// Last updated: 24/05/2025, 12:53:08
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {

    return function() {
        console.log(n)
        return n++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */