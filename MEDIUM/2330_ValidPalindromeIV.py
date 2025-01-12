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

"""