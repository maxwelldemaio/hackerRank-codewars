/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    if (s.length === 1) return 0;
    let frequencies = {};

    // Create frequency map
    for (let char of s) {
        if (frequencies[char] === undefined) {
            frequencies[char] = 1;
        } else {
            frequencies[char]++;
        }
    }

    // Find first unique character if any exist
    for (let i = 0; i < s.length; i++) {
        if (frequencies[s[i]] === 1){
            return i;
        }
    }
    return -1;
};

console.log(firstUniqChar("leetcode"));