# YouTube Video: https://www.youtube.com/watch?v=TC7apM-xGaU
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

# Import Stack class from stack.py
from stack import Stack

# Loop through chars of string
# If we encounter opening paren, push to stack
# If we encounter closing paren, pop stack and check if it matches it
# If we go through and end w/ an empty stack and no errors, balanced

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            # Opening paren, push to stack
            s.push(paren)
        else:
            # Check if there were no open parens at all
            if s.items == []:
                is_balanced = False
            else:
                # Stack is not empty
                # pop top element of stack and compare
                top = s.pop()
                # Compare top and element we are on
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    # Final check
    if s.items == [] and is_balanced:
        return True
    else:
        return False

def main():
    print(is_paren_balanced("()"))
    print(is_paren_balanced("(()"))

if __name__ == "__main__":
    main()
