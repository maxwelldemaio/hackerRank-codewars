/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // Initialize pointers
    let a = m - 1;
    let b = n - 1;
    let c = nums1.length - 1;

    for (c; c >= 0; c--){
        if (b < 0){
            break;
        }

        // Compare
        if (nums1[a] > nums2[b]){
            nums1[c] = nums1[a];
            a--;
        } else {
            nums1[c] = nums2[b];
            b--;
        }
    }
    return nums1;
};

// Test cases
// Should return [1,2,2,3,5,6]
console.log(merge([2,0], 1, [1], 1))