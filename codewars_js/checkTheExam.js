/*
Check the Exam

The first input array contains the correct answers to an 
exam, like ["a", "a", "b", "d"]. The second one is "answers" 
array and contains student's answers.

The two arrays are not empty and are the same 
length. Return the score for this array of answers, 
giving +4 for each correct answer, -1 for each incorrect answer, 
and +0 for each blank answer(empty string).

If the score < 0, return 0.

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
*/

function checkExam(array1, array2) {
    var i;
    score = 0;

    for (i = 0; i < array1.length; i++) {
        // Check if the answer was correct, incorrect, or blank
        if (array1[i] === array2[i]) {
            score += 4;
        } else if (array2[i] === "") {
            score += 0;
        } else {
            score -= 1;
        }
    };
    // If the score is less than zero, return zero
    if (score < 0) {
        score = 0;
    }
    return score
};

console.log(checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
console.log(checkExam(["b", "c", "b", "a"], ["", "a", "a", "c"]))
