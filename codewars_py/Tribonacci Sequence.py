"""
Regular Fibonacci

[1,1,2,3,5,8,13,21]

First two terms are ones, thereafter the term is equal to
the sum of the previous two terms.

Goal: write a function to return the nth term of
the Fibonacci Sequence
"""

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        # Return the sum of the previous two terms
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
    print(n, ":", fibonacci(n))

"""
Now for the bigger challenge:
Fibonacci's bigger brother, Tribonacci

As the name may already reveal, it works basically 
like a Fibonacci, but summing the last 3 (instead of 2) 
numbers of the sequence to generate the next.

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
[3, 2, 1, 6, 9, 16, 31, 56, 103, 190] etc.
"""


def tribonacci(signature, n):
    sequence = []
    # Return the sequence of every xth term of the sequence
    for x in range(0, n):
        if x == 0:
            sequence.append(signature[x])
        elif x == 1:
            sequence.append(signature[x])
        elif x == 2:
            sequence.append(signature[x])
        else:
            sequence.append(sequence[x-1] + sequence[x-2] + sequence[x-3])
    return sequence

print(tribonacci([0, 0, 1], 10))
