// Last updated: 24/05/2025, 17:12:05
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {

    returnedArray = [] // create new array 

    for (let i = 0; i < arr.length; i++) { 
        returnedArray [i] = fn(arr[i],i);
    }
    return returnedArray;
};