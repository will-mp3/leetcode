"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation 

(also known as the Hamming weight).
"""

class simpleSolution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res

"""
i have two solutions here, both are practical given the input size but the simpleSolution technically is less efficient.
the way the simple solution works is while n != 0 (there are still 1s present) a loop runs.
within this loop two things are happening:
1. the result is incremented if there is a 1 as the rightmost digit.
2. n is bit shifted over 1 bit.
what this does is checks for a 1 on the end, counts it, then moves the next digit into that same end position to be evaluated.
this solution runs in O(n) linear time.

the complex solution uses more advanced bit manipulation.
the same while loop is present, however the inner logic has now changed:
1. the result is incremented by 1 with every iteration of the loop.
2. n is now bit manipulated with a logic AND operator.
the way this bit manipulation works is best described visually.
consider n = 100001 is our input int.
on first iteration n is set equal to 100001 & 100000 and res is incremented by 1.
when evaluated n is now equal to 100000.
next iteration n is set equal to 100000 & 011111 and res is again incremented by 1.
our new value for n is 000000, breaking the loop and returning the result.
this specific solution is extremely powerful because it will only iterate for however many 1s are present.
this solution runs in O(1) constant time.
"""