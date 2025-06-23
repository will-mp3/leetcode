"""
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, 
which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, 
which does not read the same both forward and backward.

Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
"""

# first solution attempt, TLE 73/97 (easiest to understand)
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        # helper function to convert base-10 number to base-k
        def convert(num, base):
            if num == 0:
                return '0'
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        # helper function to determine palindrome
        def isPalindrome(num):
            strNum = str(num)
            strRev = strNum[::-1]

            return strNum == strRev
        
        # main logic
        cur, res = 1, 0

        while n:
            if isPalindrome(cur):
                if isPalindrome(convert(cur, k)):
                    res += cur
                    n -= 1
            cur += 1
        
        return res

"""

"""