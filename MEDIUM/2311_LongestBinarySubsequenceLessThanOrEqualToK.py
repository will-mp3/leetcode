"""You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting 
some or no characters without changing the order of the remaining characters.
"""

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if int(s[i] + res, 2) > k:
                continue
            else: 
                res = s[i] + res

        return len(res)

"""

"""