"""
You are given a 0-indexed string s consisting of only lowercase English letters. 
In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.
"""

class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0

        # odd length strings
        if len(s) % 2 != 0:
            l, r = (len(s) // 2), (len(s) // 2)
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    count += 1
                l -= 1
                r += 1
        # even length strings
        else:
            l, r = (len(s) // 2) - 1, (len(s) // 2)
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    count += 1
                l -= 1
                r += 1
        
        return True if count <= 2 else False

"""
This problem asks that we analyze a potential palindrome, specifically seeing if its possible to be made with two character conversions.
this first thing we need to understand is that we can check a palindrome by expanding pointers left and right from the center.
the next thing that we must understand is that if at any point the values at these pointers are not equal, 1 conversion must be made.
knowing these, and account for even and odd length strings, we create two pointers and a count variable.
for our odd length strings, left and right start at the same index in the center.
as they expand out, and while their index is valid, we check to see if the values at their positions are equal.
if these values are not equal, we increment our count value.
we repeat this logic for even length strings, this time setting the left pointer one index left.
we return true if our count value is less than or equal to 2 and false otherwise.
this solution runs in O(n) linear time.
"""