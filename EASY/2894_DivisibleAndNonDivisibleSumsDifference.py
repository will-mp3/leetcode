"""
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i 
            else: 
                num2 += i
        return num1 - num2

"""
this solution makes use of the modulo operator to separate divisible numbers.
we have to check through the entire list regardless, so we go through number 1 through n (inclusive).
our iterator i will be the current value we are checking, each loop we use the modulo operator to check if i is divisible by m.
this is done with a simple fi else statement since i cannot be both divisible and non-divisible.
at the end we return the sum of num1 - num2.
this solution runs in O(n) linear time.
"""