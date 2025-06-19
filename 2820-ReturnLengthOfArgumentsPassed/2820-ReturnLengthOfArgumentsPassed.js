// Last updated: 19/06/2025, 22:32:01
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let i = 0; 
    for (const item of args) { 
        i++;
    } 
    return i;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */