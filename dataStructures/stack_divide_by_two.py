"""
Use a stack data structure to convert integer values
to binary.

Example: 242
(// divides but throws away the fractional component)
242 // 2 = 121 -> Remainder:0

121 // 2 = 60 -> Remainder:1
60 // 2 = 30 -> Remainder:0
30 // 2 = 15 -> Remainder:0
15 // 2 = 7 -> Remainder:1
7 // 2 = 3 -> Remainder:1
3 // 2 = 1 -> Remainder:1
1 // 2 = 0 -> Remainder:1

"""

# Push each remainder onto the stack
# Pop each off @ end and that gives the binary representation

from stack import Stack

# Function to convert decimal into binary
def div_by_2(dec_num):
    # Create stack object
    s = Stack()

    # While the decimal number passed as the arg isn't 0 yet
    while dec_num > 0:
        # Store the remainder by pushing it to the stack
        remainder = dec_num % 2
        s.push(remainder)
        # Set the decimal number to itself floor divided by two
        dec_num = dec_num // 2

    # Go back through the Stack (top down) by popping
    # Append popped binary to a string until the Stack object is empty
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
        
    return bin_num

print(div_by_2(242))