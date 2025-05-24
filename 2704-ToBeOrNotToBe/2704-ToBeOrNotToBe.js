// Last updated: 24/05/2025, 12:33:30
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init; 
    const original = init; 

    var increment = function(){ 
        return ++count; 
    }

    var decrement = function (){
        return --count; 
    }

    var reset = function (){ 
        count = original; 
        return original; 
    }
    
    return {increment,decrement, reset}; 
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */