// Last updated: 25/05/2025, 01:45:24
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length === 0) { 
        return init; 
    } 

    var currSum = init; 

    // nums.forEach(fn)


    for (let i = 0; i < nums.length; i++){ 
        //fruits.forEach(myFunction);
        currSum = fn(currSum, nums [i])
    }

    return currSum;
    
};