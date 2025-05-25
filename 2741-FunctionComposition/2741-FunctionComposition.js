// Last updated: 25/05/2025, 14:09:28
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        // edge case 
        if (functions.length === 0) { 
            return x 
        }
        var temp = x; 

        for (let i = functions.length-1; i >= 0; i--){ 
            console.log("temp now is", temp); 
            console.log("current fn is", functions [i]); 
            temp = functions [i] (temp); 
        }

        // wanna try recursion ? 
        return temp; 

    }   
    
        
    
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */