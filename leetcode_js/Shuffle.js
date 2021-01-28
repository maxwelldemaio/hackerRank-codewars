/*Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Great explanation of shuffle: https://bost.ocks.org/mike/shuffle/
*/

/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.nums = nums;
    this.copyNums = [...nums];
};

/**
 * Resets the array to its original configuration and return it.
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    return this.copyNums;
};

/**
 * Returns a random shuffling of the array.
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
  var m = this.nums.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = this.nums[m];
    this.nums[m] = this.nums[i];
    this.nums[i] = t;
  }

  return this.nums;
};


// Your Solution object will be instantiated and called as such:
var obj = new Solution([1,2,3,4])
var param_1 = obj.reset()
var param_2 = obj.shuffle()

console.log(param_1, param_2);