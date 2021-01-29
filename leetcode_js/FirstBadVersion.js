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
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let start=0, end=n; 
        let badFound = false;
        
        while(start <= end){ 
    
            // Find the mid index 
            let mid=Math.floor((start + end)/2); 
    
            if (isBadVersion(mid)){
                // Bad version found (look left for more bads)
                badFound = true;
                end = mid - 1;
            } else if (badFound && !isBadVersion(mid)) {
                // If bad version already found, no bad now (look right)
                start = mid + 1;
            } else if (!badFound && !isBadVersion(mid)) {
                // No bad version found yet, no bad now (look right)
                start = mid + 1; 
            }     
        }
        // both end and start meet, return either
        return start;
    }
};

// Test cases
console.log(solution(5));