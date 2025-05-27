// Last updated: 27/05/2025, 13:43:30
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {

    // var delay = (millis) => {
    //     var date = new Date();
    //     while (new Date() - date < millis) { }
    // };


    return new Promise ((resolve) => { 
        setTimeout (resolve, millis);
        // resolve("anything")

    }); 


    // let t = Date.now();
    // sleep(millis).then(() => {
    //     new Promise ((resolve, reject) => { 
    //         resolve(1); 
    //     });
    //     // Date.now() - t); // 100
    // });
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */