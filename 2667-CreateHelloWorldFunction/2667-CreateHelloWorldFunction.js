// Last updated: 23/05/2025, 21:12:14
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */