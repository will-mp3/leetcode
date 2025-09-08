"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.
"""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n // 2
        b = n - a
        zeros = str(a).count("0") + str(b).count("0")
        
        while zeros > 0:
            a += 1
            b -= 1
            zeros = str(a).count("0") + str(b).count("0")
        
        return [a, b]

"""

"""