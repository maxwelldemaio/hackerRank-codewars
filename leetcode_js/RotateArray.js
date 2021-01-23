/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

0(k) time complexity
0(1) space complexity (same for all inputs since no allocation)
 */

var rotate = function (nums, k) {
    if (k === nums.length) {
        return nums;
    } else if (k > nums.length) {
        k = k % nums.length;
    }

    for (let i = 0; i < k; i++) {
        nums.unshift(nums.pop());
    };
    return nums;
};

let example = [1, 2, 3, 4, 5, 6, 7]
console.log(rotate(example, 3));