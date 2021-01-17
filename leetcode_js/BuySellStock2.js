/**
 * @param {number[]} prices
 * @return {number}
 */

/* The solution is correct not because you are selling on the 
days which are higher than the previous day but 
rather the loop adds up all potential gains. */

var maxProfit = function (prices) {
    if (prices.length <= 1) {
        return 0;
    }

    let profit = 0;
    // Sum all potential gains
    // Check all days on which we should have bought/sold
    for (var i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }
    return profit;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
// console.log(maxProfit([1, 2, 3, 4, 5]));
// console.log(maxProfit([5, 7, 100]));
