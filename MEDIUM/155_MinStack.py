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
this solution requires us to implement a stack, which is easy enough using arrays, with an added twist of also tracking the minimum value.
this problem wouldnt be so difficult if it werent for the pop function, potentially removing our min value.
to account for this, each pushed value will also be accompanied by its minimum value in the stack below it, whether that be itself or another.
when we push an element, we first check to see if the stack is empty.
if thats the case we know the value being pushed is the minimum so we append the pair (val, val).
index 0 is our value, index 1 is our minimum, once added we return so as to avoid any errors.
if we push and the stack if not empty, we set our current min equal to the last elements index 1.
we then append the pair of our value, and the minimum between the value being appended and current min.
what this does is repeatedly check and update minimum values as they are added, keeping constant time.
when we want to pop we use the standard pop method.
when we want to get the top we return the 0 index of the top value which contains the actual elements value.
when we want to get the min we return the 1 index of the top value which contains the elements min.
this solution runs in complement O(1) constant time.
"""