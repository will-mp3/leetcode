"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # use append
        # we are storing the values in the stack along with the minimum value at that point

        # if stack is empty, val is the min val
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1] # update current min based on top value
        self.stack.append((val, min(val, current_min))) # when adding this new value, update its min compared to the current min

    def pop(self) -> None:
        # use pop
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] # top elements value

    def getMin(self) -> int:
        return self.stack[-1][1] # top elements min

"""

"""