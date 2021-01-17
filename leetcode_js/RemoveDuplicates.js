/**
 * @param {number[]} nums
 * @return {number}
 */

var removeDuplicates = function (nums) {
    var pointer = 1;
    for (var i = 0; i < nums.length - 1; i++) {
        // Check for duplicates in adjacent
        // Basically at the end of the operation
        // From index 0 to pointer, there will be a unique set
        // We only need to return the length aka the pointer
        // (That's why we increment pointer)
        if (nums[i] !== nums[i + 1]) {
            nums[pointer] = nums[i + 1];
            pointer++;
        }
    }
    return pointer;
};

console.log(removeDuplicates([0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))