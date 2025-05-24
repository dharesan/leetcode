// Last updated: 24/05/2025, 12:53:16
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    var toBe = function(val2) { 
        if (val === val2) { 
            return true; 
        } 
        throw new Error ("Not Equal")
    };
    
    var notToBe = function(val2){
        if (val !== val2) { 
            return true;
        }
        throw new Error("Equal")
    };

    return {toBe,notToBe};

};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */