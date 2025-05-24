// Last updated: 24/05/2025, 17:30:34
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    filteredArr = []; 

    for (let i = 0; i < arr.length; i++) { 
        // filteredArr [i] = fn(arr[i], i); 
        var temp = fn(arr[i], i); //boolean value 
        if (temp) { 
            console.log("entered")
            filteredArr.push(arr[i]);
        } 

    }

    return filteredArr;
};