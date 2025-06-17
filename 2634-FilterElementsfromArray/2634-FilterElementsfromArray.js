// Last updated: 17/06/2025, 14:19:36
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