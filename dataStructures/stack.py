"""
Stack Data Structure
link: https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV
"""

""""
Pretend this is a stack of books
Pushed in the order: A,B,C,D
Popping is taking something off the top of the stack

D
C
B
A
"""

class Stack():
    def __init__(self):
        self.items = []

    # Push given item to top of stack
    def push(self, item):
        self.items.append(item)

    def pop(self):
        # Returns top element of stack and pops it off
        return self.items.pop()

    def is_empty(self):
        # Return boolean if stack is empty
        return self.items == []

    def peek(self):
        # Look at top most element of stack
        # Only if the object has values
        if not self.items == []:
            return self.items[-1]

    def get_stack(self):
        return self.items

def main():
    # s is a Stack object
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    print(s.peek())
    print(s)

if __name__ == "__main__":
    main()
