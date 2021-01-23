/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    let left = 0;
    let right = s.length - 1;

    while(left < right) {
        let temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
};

let test1 = ["h", "e", "l", "l", "o"]
let test2 = ["H", "a", "n", "n", "a", "h"]

reverseString(test1);
console.log(test1);