"""
You have n dice, and each dice has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. 
Since the answer may be too large, return it modulo 109 + 7.
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1 # base case

            if (n, target) in memo: # if we have seen this combo return the value saved
                return memo[(n, target)]

            res = 0

            # calculate new target values for passing
            # range will always be size k unless target is less than k
            # when target is less than k we know the excluded values could not be valid
            # example: target = 3, k = 6. we have values up to 6 but are looking to find equal 3
            # instead of wasting time seeing if 4 equals 3 we just include values 3, 2, 1 which give us new targets 0, 1, 2
            for i in range(max(0, target-k), target):
                res += dp(n-1, i)

            # save the value at n dice remaining for target
            memo[(n, target)] = res

            return res

        return dp(n, target) % (10**9 + 7)
    
"""

"""