"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]

"""
for this problem we use a bottom up dynamic programming algorithm.
the idea is that instead of trying to find how many perfect squares make up n, we start at 0 and work our way backwards.
for example if n = 12, we would instead start at n = 0, then n = 1, then n = 2, and so on.
the minimum squares is stored in our dp array, whose index represents the above n values, and is repeatedly updated.
what this does for us is create an array of minimum squares for each value.
when we get to a new target we can check to see if there is a shorter path that we have already stored and update the array.
to start we create a dp array of size n + 1 which is filled with our n value (n value is used so we can work with minimums later).
we initiliaze position zero to 0 as our base case.
next we iterate through every position (target) in our dp array, and for each target we iterate through values (s) from 1 to the target.
for each iteration we calculate the square of our current s value.
we check to see if the square is too large, if so we immediately break the inner loop and continue the outer loop.
if the square is small enough we then check to update our dp array.
to do this we check the minimum between the target indexes current element 
and that of the target - square + 1 (since we have to include the current step).
once the outer loop completes we can return the value stored at element n since our indexes represent our values.
this solution runs in O(n * sqrt(n)).
"""