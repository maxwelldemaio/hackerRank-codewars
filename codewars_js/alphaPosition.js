/*
Replace With Alphabet Position

In this kata you are required to, given a string, replace every 
letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabetPosition("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" 
(as a string)
*/

function alphabetPosition(text) {
    var result = "";
    // Convert string to upper case
    text = text.toUpperCase();

    // Check if char is valid and append number to result
    for (var x = 0; x < text.length; x++) {
        var ascii = text.charCodeAt(x);
        if (ascii > 64 && ascii < 91) result += (ascii - 64) + " ";
    }
    // Remove trailing space @ end
    return result.slice(0, result.length - 1);;
}

// Tests
console.log(alphabetPosition("The sunset sets at twelve o' clock."));
