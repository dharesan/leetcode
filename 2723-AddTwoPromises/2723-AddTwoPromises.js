// Last updated: 26/05/2025, 17:56:12
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {

    let value1 = await promise1; 
    let value2 = await promise2; 
    const result = value1 + value2; 

    // promise1.then(value1 => { 
    //     //console.log(value);
    //     const valueUse1 = value1; 
    //     console.log(value1);
    // }); 


    // promise2.then(value2 => { 
    //     //console.log(value);
    //     const valueUse2 = value2; 
    //     console.log(value1);
    // }); 

    // const result = valueUse1 + valueUse2; 
    return new Promise(resolve => setTimeout(() => resolve(result), 30))

    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */