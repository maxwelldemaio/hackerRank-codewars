/*
Coefficients of the Quadratic Equation

In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).

Equation will be the form of ax^2 + bx + c = 0

Return type is a Vector containing coefficients of the equations in the order (a, b, c).

Since there are infinitely many solutions to this problem, we fix a = 1.

Ex) quadratic(1,2) = (1, -3, 2)
This means (x-1) * (x-2) = 0; 
when we do the multiplication this becomes x^2 - 3x + 2 = 0
*/

// What two numbers multiply to equal c, which also sum to b?

function quadratic(x1, x2) {
    // Answer in array
    root1 = (-1 * x1);
    root2 = (-1 * x2);
    bTerm = root1 + root2;
    cTerm= root1 * root2;
    return [1, bTerm, cTerm];
};

console.log(quadratic(1,2));