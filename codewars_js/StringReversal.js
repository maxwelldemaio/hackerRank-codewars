/*
Simple string reversal

In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.
*/

function reverseWords(str) {
    spacePositions = []
    strArray = str.split("")
    // Loop over array of letters
    // Store indexes for spaces
    for (var x=0; x < strArray.length; x++) {
        if (strArray[x] === " ") {
            spacePositions.push(x);
        }
    }
    // Pop spaces from strArray
    for (var x = 0; x < strArray.length; x++) {
        if (strArray[x] === " ") {
            strArray.splice(x, 1);
        }
    }
    // Reverse the array of letters
    // Insert spaces back into the array
    strArray.reverse()
    for (var x=0; x < spacePositions.length; x++) {
        strArray.splice(spacePositions[x], 0, " ");
    }
    return strArray.join("")
}

console.log(reverseWords("The quick brown fox jumps over the lazy dog."));
