/*
Array.diff

Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

arrayDiff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

arrayDiff([1,2,2,2,3],[2]) == [1,3]
*/

function arrayDiff(a, b) {
    newArray = [];

    // Loop over array A and push items that aren't in array B to the newArray
    for (var x=0; x < a.length; x++) {
        notInArray = true;
        for (var y =0; y < b.length; y++) {
            if (a[x] === b[y]) {
                notInArray = false;
            }
        }
        if (notInArray) {
            newArray.push(a[x]);
        }
    }
    return newArray;
}

// Test cases
arrayDiff([3, 4], [3])
arrayDiff([1, 8, 2], [])
arrayDiff([1, 2, 2, 2, 3], [2])
arrayDiff([], [4, 5])