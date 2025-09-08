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
This code defines a solution to find two No-Zero integers that sum up to a given integer n. A No-Zero integer is defined as a positive integer that does not contain the digit '0' in its decimal representation.
The function `getNoZeroIntegers` takes an integer n as input and returns a list containing two No-Zero integers [a, b] such that a + b = n. The approach used in this solution is as follows:
1. It starts by initializing `a` to half of `n` (using integer division) and `b` to the difference between `n` and `a`. This ensures that and b are as close to each other as possible, which is a good starting point for finding No-Zero integers.
2. It then calculates the number of '0' digits in both `a` and `b` by converting them to strings and counting the occurrences of '0'.
3. If either `a` or `b` contains '0', the code enters a while loop that continues until both integers are No-Zero integers (i.e., the count of '0' digits is zero). Inside the loop, it increments `a` by 1 and decrements `b by 1, effectively adjusting the pair while maintaining their sum equal to `n`.
4. After each adjustment, it recalculates the count of '0' digits in both integers.
5. Once both integers are No-Zero integers, the loop exits, and the function returns the list [a, b].
The time complexity of this solution is O(k), where k is the number of adjustments needed to find No-Zero integers. In the worst case, this could be proportional to n, but typically it will be much smaller. The space complexity is O(1) since only a constant amount of extra space is used for the variables.
"""