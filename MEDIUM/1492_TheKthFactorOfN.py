"""
You are given two positive integers n and k. 
A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        x = 1

        while x <= n:
            if n % x == 0:
                factors.append(x)
            x += 1
        
        if len(factors) < k:
            return -1
        
        return factors[k - 1]

"""
this problem asks us to find the kth factor of a given integer.
to solve this problem, we must find a way to compile the factors of int n into a last of sorts.
to do this, we intialize a result list as well as a variable x, x will be used to find the factors of n.
we loop while x is less than n, each time moding x by n and checking if it equals zero.
if n % x == 0, then we know that n is divisible by x, and x is a factor.
once the loop completes, we check to see if there are atleast k factors in our array, if not we return -1.
otherwise, we return the kth index of our array.
this solution runs in O(n) linear time.
"""