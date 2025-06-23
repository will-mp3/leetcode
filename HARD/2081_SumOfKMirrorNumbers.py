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
    
# second, working solution (includes optimization)
    class Solution:
        def createPalindrome(self, num: int, odd: bool) -> int:
            x = num
            if odd:
                x //= 10
            while x > 0:
                num = num * 10 + x % 10
                x //= 10
            return num

        def isPalindrome(self, num: int, base: int) -> bool:
            digits = []
            while num > 0:
                digits.append(num % base)
                num //= base
            return digits == digits[::-1]

        def kMirror(self, k: int, n: int) -> int:
            total = 0
            length = 1
            while n > 0:
                for i in range(length, length * 10):
                    if n <= 0:
                        break
                    p = self.createPalindrome(i, True)
                    if self.isPalindrome(p, k):
                        total += p
                        n -= 1
                for i in range(length, length * 10):
                    if n <= 0:
                        break
                    p = self.createPalindrome(i, False)
                    if self.isPalindrome(p, k):
                        total += p
                        n -= 1
                length *= 10
            return total

"""
this one is annoying, I would just focus on my first answer instead of the working one.
"""