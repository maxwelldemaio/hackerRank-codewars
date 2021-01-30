// Test API
function isBadVersion(num){
    if (num >= 4) {
        return true;
    }
}

/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(api) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let start=1; 
        let end=n; 
        while(start <= end){ 
            // Find the mid index 
            let mid=Math.floor((start + end)/2); 
    
            if (isBadVersion(mid)){
                // Bad version found (look left for more bads)
                end = mid - 1;
            } else {
                // If bad version already found, no bad now (look right)
                // No bad version found yet, no bad now (look right)
                start = mid + 1;
            }    
        }
        // Start is ontop of first bad instance
        return start;
    }
};

// Test cases
console.log(solution(isBadVersion)(5));