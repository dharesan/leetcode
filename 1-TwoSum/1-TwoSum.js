// Last updated: 22/05/2025, 14:44:06
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // input: nums is an array 
    // input: target is an integer 

    const result = []; // Creates an empty array

    for (let i = 0; i < nums.length; i++) { 
        let copyArray = nums.slice(); 
        let duplicateArray = nums.slice(); 
        copyArray.splice(i, 1); 
        //console.log(copyArray); 

        duplicateArray [i] = null ; 

        let currNum = nums[i]; 
        let findingNum = target - currNum; 
        for (let j=0; j < copyArray.length; j++) { 
            //console.log("findingNum is", findingNum); 
            if (copyArray[j] === findingNum) { 
                //console.log("i now is", i);
                result.push(i);
                //console.log("dup array is", duplicateArray); 
                result.push(duplicateArray.indexOf(findingNum)); 
                //console.log('result is', result); 
                return result; 
            }
    
        }
        //return result; 


    }
    //return result; 
};