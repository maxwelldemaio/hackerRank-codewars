/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    let hTable = {};
    for (let i = 0; i < nums.length; i++) {
        console.log(nums[i]);
        if (nums[i] in hTable)
            return true;
        hTable[nums[i]] = 1;
    }
    return false;
};

let test1 = [1, 2, 3, 1];
let test2 = [1, 2, 3, 4];

console.log(containsDuplicate(test2));